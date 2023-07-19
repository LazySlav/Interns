from json import dumps
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
    elif request.method == "PUT":
        try:
            # may be needed to implement with **kwargs
            obj = CompanyModel.objects.create(*request.PUT.values())
            obj.save()
            return JsonResponse(obj)
        except Exception as e:
            raise
    elif request.method == "DELETE":
        pass


def post_profile(request: HttpRequest):
    try:
        # may be needed to implement with **kwargs
        data = request.POST.dict()
        CompanyModel.objects.create(**data)
        return JsonResponse(data,status=201)
    except Exception as e:
        raise
