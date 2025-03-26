from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacancie
from django.core.paginator import Paginator

def home(request):
  return render(request, template_name="home.html" )

# VER TODAS AS VAGAS
def view_vacancies(request):

  # Pegando todos os Objetos - Ordenados pelo "id maior na frente"
  vacancie = Vacancie.objects.all().order_by("-id")

  # Instancia do paginator
  vacancie_paginator = Paginator(vacancie, 12)

  # Definindo pagina atual
  page_num = request.GET.get('page')

  # Passa o meu objeto listado
  page = vacancie_paginator.get_page(page_num)

  for item in page:
    print(item.state)

  context = {
    'page': page,
    'vacancie_paginator': vacancie_paginator
  }

  return render(request, template_name="view_vacancies.html", context=context)

# VER APENAS UMA AS VAGA
def view_one_vacancie(request, id):

  vacancie = Vacancie.objects.get(id=id)

  context = {'vacancie': vacancie}

  return render(request, template_name='view_one_vacancie.html', context=context)

def about(request):
  return render(request, template_name="about.html" )
