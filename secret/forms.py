from django import forms
from django.contrib.auth.forms import UserCreationForm

from jobs.models import Vacancie, Enterprise

class VacancieForm(UserCreationForm):
  
  TYPE_MODALITY = (
    ("CLT - Efetivo",     'CLT - Efetivo'),
    ("CLT - Ferista",     'CLT - Ferista'),
    ("CLT - Contrato",    'CLT - Contrato'),
    ("AVULSO - Diaria",   'AVULSO - Diaria'),
    ("AVULSO - Semanal",  'AVULSO - Semanal'),
    ("AVULSO - Quinzena", 'AVULSO - Quinzena'),
    ("CNPJ - Prestação de serviço",  'CNPJ - Prestação de serviço'),
  )

  TYPE_JOURNEY = (
    ("Escala - 5x1",      'Escala - 5x1'),
    ("Escala - 5x2",      'Escala - 5x2'),
    ("Escala - 6x1",      'Escala - 6x1'),
    ("Escala - 12x36",    'Escala - 12x36'),
    ("Escala - 18x36",    'Escala - 18x36'),
    ("Diaria - 1 Dia",    'Diaria - 1 Dia'),
    ("Diaria - 7 Dias",   'Diaria - 7 Dias'),
    ("Diaria - 15 Dias",  'Diaria - 15 Dias'),
  )

  TYPE_STATE = (
    (True,'Vaga aberta'),
    (False,'Vaga fechada'),
  )

  title = forms.CharField(
      empty_value=False,
      max_length=255,
      widget=forms.TextInput(
        attrs={
          'class': 'block w-full p-2 rounded-sm  text-myGreen-800 outline outline-1 -outline-offset-1 outline-myGreen-300 placeholder:text-myWhite-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-myGreen-400 duration-300 text-sm/6',
          'placeholder': 'Informe o titulo da sua vaga...'
        }
    )
  )

  email = forms.CharField(
    empty_value=False,
    required=True,
    widget=forms.EmailInput(
      attrs={
        'class': ' block w-full p-2 rounded-sm  text-myGreen-800 outline outline-1 -outline-offset-1 outline-myGreen-300 placeholder:text-myWhite-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-myGreen-400 duration-300 text-sm/6',
        'placeholder': 'Informe seu melhor email'
      }
    )
  )


  whatsapp = forms.CharField(
      empty_value=False,
      max_length=14,
      widget=forms.TextInput(
        attrs={
          'class': ' block w-full p-2 rounded-sm  text-myGreen-800 outline outline-1 -outline-offset-1 outline-myGreen-300 placeholder:text-myWhite-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-myGreen-400 duration-300 text-sm/6',
          'placeholder': 'WhatsApp para contato...'
        }
    )
  )

  wage = forms.CharField(
      empty_value=False,
      widget=forms.TextInput(
        attrs={
          'class': ' block w-full p-2 rounded-sm  text-myGreen-800 outline outline-1 -outline-offset-1 outline-myGreen-300 placeholder:text-myWhite-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-myGreen-400 duration-300 text-sm/6',
          'placeholder': 'Valor do salário...'
        }
    )
  )

  modality = forms.CharField(
      empty_value=False,
      widget=forms.Select(
        choices=TYPE_MODALITY,
        attrs={
          'class': ' block w-full p-2 rounded-sm  text-myGreen-800 outline outline-1 -outline-offset-1 outline-myGreen-300 placeholder:text-myWhite-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-myGreen-400 duration-300 text-sm/6',
          'placeholder': 'Modalidade de trabalho...'
        }
    )
  )

  weekly_journey = forms.CharField(
      empty_value=False,
      widget=forms.Select(
        choices=TYPE_JOURNEY,
        attrs={
          'class': ' block w-full p-2 rounded-sm  text-myGreen-800 outline outline-1 -outline-offset-1 outline-myGreen-300 placeholder:text-myWhite-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-myGreen-400 duration-300 text-sm/6',
          'placeholder': 'Jornada de trabalho...'
        }
    )
  )

  work_shift = forms.CharField(
      empty_value=False,
      widget=forms.TextInput(
        attrs={
          'class': ' block w-full p-2 rounded-sm  text-myGreen-800 outline outline-1 -outline-offset-1 outline-myGreen-300 placeholder:text-myWhite-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-myGreen-400 duration-300 text-sm/6',
          'placeholder': 'Informe o turno de trabalho'
        }
    )
  )

  state = forms.CharField(
      empty_value=False,
      widget=forms.Select(
        choices=TYPE_STATE,
        attrs={
          'class': 'block w-full p-2 rounded-sm  text-myGreen-800 outline outline-1 -outline-offset-1 outline-myGreen-300 placeholder:text-myWhite-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-myGreen-400 duration-300 text-sm/6',
          'placeholder': 'Você está já está contratando...'
        }
    )
  )

  description = forms.CharField(
      empty_value=False,
      widget=forms.Textarea(
        attrs={
          'class': ' block w-full p-2 rounded-sm  text-myGreen-800 outline outline-1 -outline-offset-1 outline-myGreen-300 placeholder:text-myWhite-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-myGreen-400 duration-300 text-sm/6',
          'placeholder': 'Preencha caso tenha mais informações especificações sobre a sua vaga de trabalho...'
        }
    )
  )

  class Meta(UserCreationForm.Meta):
    model = Enterprise
    fields = ("__all__")

class RecoveryPasswordForm(UserCreationForm):

  email = forms.CharField(
    empty_value=False,
    required=True,
    widget=forms.EmailInput(
      attrs={
        'class': 'block w-full p-2 rounded-sm  text-myGreen-800 outline outline-1 -outline-offset-1 outline-myGreen-300 placeholder:text-myWhite-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-myGreen-400 duration-300 text-sm/6',
        'placeholder': 'Informe o email da sua conta...'
      }
    )
  )

  password = forms.CharField(

    widget=forms.PasswordInput(
      attrs={
        'class': ' block w-full p-2 rounded-sm  text-myGreen-800 outline outline-1 -outline-offset-1 outline-myGreen-300 placeholder:text-myWhite-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-myGreen-400 duration-300 text-sm/6',
        'placeholder': 'Informe uma senha...'
      }
    )
  )

  password2 = forms.CharField(

    widget=forms.PasswordInput(
      attrs={
        'class':' block w-full p-2 rounded-sm  text-myGreen-800 outline outline-1 -outline-offset-1 outline-myGreen-300 placeholder:text-myWhite-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-myGreen-400 duration-300 text-sm/6',
        'placeholder': 'Confirme sua nova senha...'
      }
    )
  )

  class Meta(UserCreationForm.Meta):
    model = Enterprise
    fields = ("__all__")