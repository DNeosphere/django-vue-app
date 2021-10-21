from django.urls import path
from .views import CompanyView, IMCView

urlpatterns= [
  path('companies/', CompanyView.as_view(), name='companies_list'),
  path('imc/', IMCView.as_view(), name='imc_entries_list')
]