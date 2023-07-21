import ast
import json
from uuid import UUID
from django.forms import ValidationError
from django.http import HttpRequest, JsonResponse
from web.models import CompanyModel
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder


def __parse_request(request: HttpRequest):
    if (data:=request.body.decode('utf-8')) is not "":
        return ast.literal_eval(request.body.decode('utf-8'))
    return dict()


def __parse_model(obj: models.Model):
    data = obj.__dict__
    data.pop("_state")
    return data


def __id_check(id):
    if not id:
        raise ValidationError("No id provided")


def main(request: HttpRequest, id: UUID | None = None):

    if request.method == 'GET':
        id = __parse_request(request).get("id",None)
        if id:
            try:
                obj = CompanyModel.objects.get(id=id)
            except (CompanyModel.DoesNotExist, CompanyModel.MultipleObjectsReturned):
                raise
            data = __parse_model(obj)
            return JsonResponse(data)
        else:
            # company_list = list(CompanyModel.objects.all().values())
            # company_dict = json.dumps(company_list, cls=DjangoJSONEncoder)
            # print(company_dict)
            # return JsonResponse({"companies":company_dict})

    elif request.method == "POST":
        data = __parse_request(request)
        obj = CompanyModel(**data)
        try:
            obj.full_clean()
        except ValidationError as e:
            raise
        obj.save()
        data["id"] = obj.id
        return JsonResponse(data, status=201)

    elif request.method == "PUT":
        id = __parse_request(request)["id"]
        __id_check(id)
        try:
            obj = CompanyModel.objects.get(id=id)
        except (CompanyModel.DoesNotExist, CompanyModel.MultipleObjectsReturned) as e:
            raise
        data = __parse_request(request)
        data.pop("id")
        {setattr(obj, attr, val) for attr, val in data.items()}
        obj.save(update_fields=data.keys())
        return JsonResponse({"msg": f"Successfully updated entry with id={id}"}, status=200)

    elif request.method == "DELETE":
        id = __parse_request(request)["id"]
        __id_check(id)
        try:
            obj = CompanyModel.objects.get(id=id)
        except (CompanyModel.DoesNotExist, CompanyModel.MultipleObjectsReturned) as e:
            raise
        obj.delete()
        return JsonResponse({"msg": f"Successfully deleted entry with id={id}"}, status=200)
