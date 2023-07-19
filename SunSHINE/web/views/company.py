from uuid import UUID
from django.http import HttpRequest, JsonResponse
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
        obj = CompanyModel.objects.create(*request.POST.values())
        obj.save()
        return JsonResponse(obj)
    except Exception as e:
        raise
