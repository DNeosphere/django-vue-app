from django.urls import path
from .views import CompanyView, IMCView, PetsView

urlpatterns= [
  path('companies/', CompanyView.as_view(), name='companies_list'),
  path('imc/', IMCView.as_view(), name='imc_entries_list'),
  path('pets/', PetsView.as_view(), name='pets_list')
]