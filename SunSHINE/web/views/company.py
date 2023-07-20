import ast
from django.forms import ValidationError
from django.http import HttpRequest, JsonResponse
from web.models import CompanyModel

# JSON_400 = JsonResponse({"msg":"Wrong request params"},status=400)
def parse_request(request : HttpRequest):
    return ast.literal_eval(request.body.decode('utf-8'))



def get_put_delete_profile(request: HttpRequest, id: int):
    if request.method == 'GET':
        try:
            return CompanyModel.objects.get(id=request.GET.get("id"))
        except (CompanyModel.DoesNotExist, CompanyModel.MultipleObjectsReturned):
            raise
    elif request.method == "POST":
        try:
            data = ast.literal_eval(request.body.decode('utf-8'))
            obj = CompanyModel.objects.get(id=id)
            {setattr(obj,attr,val) for attr,val in data.items()}
            obj.save(update_fields=data.keys())
            return JsonResponse({"msg":"Successfully updated entry with id={id}"},status=200)
        except Exception as e:
            raise
    elif request.method == "DELETE":
        try:
            CompanyModel.objects.get(id=id).delete()
            return JsonResponse({"msg":"Successfully deleted entry with id={id}"},status=200)
        except Exception as e:
            raise


def post_profile(request: HttpRequest):
    if request.method == "POST":
        data = parse_request(request)
        obj = CompanyModel(**data)
        try:
            obj.full_clean()
        except ValidationError as e:
            raise
        obj.save()
        data["id"]=obj.id
        return JsonResponse(data,status=201)
    return JsonResponse({"msg":"Wrong request method"})