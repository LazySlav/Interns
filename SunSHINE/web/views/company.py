from json import dumps
import json
from uuid import UUID
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from web.models import CompanyModel


def get_put_delete_profile(request: HttpRequest, id: UUID):
    if request.method == 'GET':
        try:
            return CompanyModel.objects.get(id=id)
        except (CompanyModel.DoesNotExist, CompanyModel.MultipleObjectsReturned):
            raise    
    elif request.method == "POST":
        try:
            data = request.POST.dict()
            obj = CompanyModel.objects.get(id=data["id"])
            {exec(f"obj.{attr}={val}") for attr,val in data.items()}
            obj.save(update_fields=data.keys())
            return JsonResponse("Successfully updated entry with id={id}")
        except Exception as e:
            raise
    elif request.method == "DELETE":
        try:
            CompanyModel.objects.get(id=id).delete()
            return JsonResponse("Successfully deleted entry with id = {id}")
        except Exception as e:
            raise


def post_profile(request: HttpRequest):
    try:
        data = request.POST.dict()
        obj = CompanyModel(**data)
        obj.save()
        data["id"]=obj.id
        return JsonResponse(data,status=201)
    except Exception as e:
        raise
