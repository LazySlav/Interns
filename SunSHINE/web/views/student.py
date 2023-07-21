import ast
from uuid import UUID
from django.forms import ValidationError
from django.http import HttpRequest, JsonResponse
from web.models import MentorModel, StudentModel
from django.db import models

def __parse_request(request: HttpRequest):
    return ast.literal_eval(request.body.decode('utf-8'))


def __parse_model(obj: models.Model):
    data = obj.__dict__
    data.pop("_state")
    return data


def __id_check(id):
    if not id:
        raise ValidationError("No id provided")


def main(request: HttpRequest, id: UUID | None = None):


    if request.method == 'GET':
        id = __parse_request(request)["id"]
        __id_check(id)
        try:
            obj = StudentModel.objects.get(id=id)
        except (StudentModel.DoesNotExist, StudentModel.MultipleObjectsReturned):
            raise
        data = __parse_model(obj)
        return JsonResponse(data)
    

    elif request.method == "POST":
        data = __parse_request(request)
        data["mentor"] = MentorModel.objects.get(id=data["mentor"])
        obj = StudentModel(**data)
        try:
            obj.full_clean()
        except ValidationError as e:
            raise
        obj.save()
        data["id"] = obj.id
        data["mentor"] = obj.mentor.id
        return JsonResponse(data, status=201)
    

    elif request.method == "PUT":
        id = __parse_request(request)["id"]
        __id_check(id)
        try:
            obj = StudentModel.objects.get(id=id)
        except (StudentModel.DoesNotExist, StudentModel.MultipleObjectsReturned) as e:
            raise
        data = __parse_request(request)
        data.pop("id")
        if (mentor_id:=data.get("mentor",None)) is not None:
            data["mentor"] = MentorModel.objects.get(id=mentor_id)
        {setattr(obj, attr, val) for attr, val in data.items()}
        obj.save(update_fields=data.keys())
        return JsonResponse({"msg": f"Successfully updated entry with id={id}"}, status=200)
    

    elif request.method == "DELETE":
        id = __parse_request(request)["id"]
        __id_check(id)
        try:
            obj = StudentModel.objects.get(id=id)
        except (StudentModel.DoesNotExist, StudentModel.MultipleObjectsReturned) as e:
            raise
        obj.delete()
        return JsonResponse({"msg": f"Successfully deleted entry with id={id}"}, status=200)