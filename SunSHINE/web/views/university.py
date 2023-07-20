import ast
from django.forms import ValidationError
from django.http import HttpRequest, JsonResponse
from web.models import UniversityTable
from django.db import models



def __parse_request(request: HttpRequest):
    return ast.literal_eval(request.body.decode('utf-8'))


def __parse_model(obj: models.Model):
    data = obj.__dict__
    data.pop("_state")
    return data


def __id_check(university):
    if not university:
        raise ValidationError("No university provided")


def main(request: HttpRequest, university: int | None = None):


    if request.method == 'GET':
        university = __parse_request(request)["university"]
        __id_check(university)
        try:
            obj = UniversityTable.objects.get(university=university)
        except (UniversityTable.DoesNotExist, UniversityTable.MultipleObjectsReturned):
            raise
        data = __parse_model(obj)
        return JsonResponse(data)
    

    elif request.method == "POST":
        data = __parse_request(request)
        obj = UniversityTable(**data)
        try:
            obj.full_clean()
        except ValidationError as e:
            raise
        obj.save()
        data["university"] = obj.university
        return JsonResponse(data, status=201)
    

    elif request.method == "DELETE":
        university = __parse_request(request)["university"]
        __id_check(university)
        try:
            obj = UniversityTable.objects.get(university=university)
        except (UniversityTable.DoesNotExist, UniversityTable.MultipleObjectsReturned) as e:
            raise
        obj.delete()
        return JsonResponse({"msg": f"Successfully deleted entry with university={university}"}, status=200)