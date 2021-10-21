from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Company
from .models import IMC

# Create your views here.
class CompanyView(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)

  def get(self, request):
    companies = list(Company.objects.values())

    if len(companies) > 0:
      data={
        'message':'Success',
        'companies':companies
      }
    else:
      data = {
        'message': 'companies not found'
      }

    return JsonResponse(data)

  def post(self, request):
    # print(request.body)
    jd = json.loads(request.body)

    #print(jd)

    Company.objects.create(
      name = jd['name'],
      website = jd['website'],
      foundation = jd['foundation']
    )

    response_data = {
      "message": "success"
    }

    return JsonResponse(response_data)

  def put(self, request):
    pass

  def delete(self, request):
    pass

class IMCView(View):
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)

  ''' Lists all IMC entries in the DB '''
  def get(self, request):
    IMC_entries = list(IMC.objects.values())

    if len(IMC_entries) > 0:
      data={
        'message':'Success',
        'IMC_entries':IMC_entries
      }
    else:
      data = {
        'message': 'IMC_entries not found'
      }

    return JsonResponse(data)

  ''' Creates a new IMC entry in DB '''
  def post(self, request):
    imc_json_data = json.loads(request.body)

    print(imc_json_data)

    IMC.objects.create(
      genre = imc_json_data['genre'],
      name = imc_json_data['name'],
      lastname = imc_json_data['lastname'],
      email = imc_json_data['email'],
      weight = imc_json_data['weight'],
      height = imc_json_data['height']
    )

    response_data = {
      "message": "success"
    }

    return JsonResponse(response_data)

  def put(self, request):
    pass

  def delete(self, request):
    pass
