from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Enterprise, Vacancie

@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):

  list_display = (
    'id', 'username', 'cnpj', 'sector',
    'email', 'whatsapp', 'is_superuser',
  )

  list_display_links = ('username',)

  search_fields = ('cnpj',)

@admin.register(Vacancie)
class VacancieAdmin(admin.ModelAdmin):
  
    list_display = ['id', 'title', ]
    list_display_links = ('title',)
    search_fields = ('title','id')
    
  
    # Adiciona uma filtragem para o usuário logado
    def get_queryset(self, request):
      
        dataRequestVacancie = super().get_queryset(request) # Retorna Todos os registros do Model Vacancie
        
        if request.user.is_superuser:
            return dataRequestVacancie  # Se a requisição for do superusuário vê todas as vagas
           
        return dataRequestVacancie.filter(enterprise=request.user)  # Usuário comum vê apenas suas vagas

    # Se você quiser que os posts sejam filtrados na interface do admin
    


