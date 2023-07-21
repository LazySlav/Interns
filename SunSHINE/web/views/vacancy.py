import ast
from uuid import UUID
from django.forms import ValidationError
from django.http import HttpRequest, JsonResponse
from web.models import CompanyModel, CuratorModel, VacancyModel
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
            obj = VacancyModel.objects.get(id=id)
        except (VacancyModel.DoesNotExist, VacancyModel.MultipleObjectsReturned):
            raise
        data = __parse_model(obj)
        return JsonResponse(data)
    

    elif request.method == "POST":
        data = __parse_request(request)
        data["company"] = CompanyModel.objects.get(id=data["company"])
        data["curator"] = CuratorModel.objects.get(id=data["curator"])
        obj = VacancyModel(**data)
        try:
            obj.full_clean()
        except ValidationError as e:
            raise
        obj.save()
        data["company"] = obj.company.id
        data["curator"] = obj.curator.id
        data["id"] = obj.id
        return JsonResponse(data, status=201)
    

    elif request.method == "PUT":
        id = __parse_request(request)["id"]
        __id_check(id)
        try:
            obj = VacancyModel.objects.get(id=id)
        except (VacancyModel.DoesNotExist, VacancyModel.MultipleObjectsReturned) as e:
            raise
        data = __parse_request(request)
        data.pop("id")
        if (company_id:=data.get("company",None)) is not None:
            data["company"] = CompanyModel.objects.get(id=company_id)
        if (curator_id:=data.get("curator",None)) is not None:
            data["curator"] = CuratorModel.objects.get(id=curator_id)
        {setattr(obj, attr, val) for attr, val in data.items()}
        obj.save(update_fields=data.keys())
        return JsonResponse({"msg": f"Successfully updated entry with id={id}"}, status=200)
    

    elif request.method == "DELETE":
        id = __parse_request(request)["id"]
        __id_check(id)
        try:
            obj = VacancyModel.objects.get(id=id)
        except (VacancyModel.DoesNotExist, VacancyModel.MultipleObjectsReturned) as e:
            raise
        obj.delete()
        return JsonResponse({"msg": f"Successfully deleted entry with id={id}"}, status=200)