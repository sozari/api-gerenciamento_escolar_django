"""
URL configuration for meuprojeto02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   #rota, view responsavel nome de referencia
    path('', views.inicial,name='inicial'),
    path('sobre',views.sobre,name='sobre'),
    path('cadastro_adm/', views.cadastro_adm,name='cadastro_adm'),
    path('cadastro_aluno/',views.cadastro_aluno,name='cadastro_aluno'),
    path('cadastro_professor/',views.cadastro_professor,name='cadastro_professor'),
    path('cadastro_turma/',views.cadastro_turma,name='cadastro_turma'),
    path('editar_notas/',views.editar_notas,name='editar_notas'),
    #path('inicial/',views.inicial,name='inicial'),
    path('lista_alunos/',views.lista_alunos,name='lista_alunos'),
    path('login/',views.login,name='login'),
    path('turma_select/',views.turma_select,name='turma_select'),
    path('usuario_list/',views.usuario_list,name='usuario_list'),

    path('turmas/cadastro/', views.mostrar_formulario_turma, name='mostrar_formulario'),
    path('turmas/cadastrar/', views.cadastro_formulario_turma, name='submit_formulario'),
    path('usuario_list', views.listar_usuarios, name='listar_usuarios'),
    path('usuario_list.html', views.listar_usuarios_html, name='usuario_list_html'),
    path('usuario_list',views.usuario_list,name='usuario_list'),
  
    
    path('usuario_listagem/', views.usuario_listagem, name='usuario_listagem'),
    path('usuario_edit/<int:idusuario>/', views.usuario_edit, name='usuario_edit'),
    # path('usuario_delete/<int:idusuario>/', views.usuario_delete, name='usuario_delete'),
    
    
    
    #path('cadastro/', views.cadastro, name='cadastro'),
    #path('editarusuario/<int:id>', views.editarusuario, name='editarusuario'),
    path('excluirusuario/<int:id>/', views.excluirusuario, name='excluirusuario'),

    
    
    
    
    path('usuario_update/<int:idusuario>/', views.usuario_update, name='usuario_update'),
    
    
    
    path('cadastro/professor/', views.mostrar_formulario_professor, name='cadastro_professor'),  # Rota para exibir o formulário
    path('cadastro/professor/', views.submit_formulario_professor, name='submit_cadastro_professor'),  # Rota para processar o formulário
    
    
    # Rota para exibir e processar o formulário de cadastro de administrador
    path('cadastro_adm/', views.mostrar_formulario_adm, name='cadastro_adm'),
    path('cadastro_adm/', views.submit_formulario_adm, name='submit_cadastro_adm'),

    # Rota para exibir e processar o formulário de cadastro de aluno
    path('cadastro/aluno/', views.mostrar_formulario_aluno, name='cadastro_aluno'),
    path('cadastro/aluno/', views.submit_formulario_aluno, name='submit_cadastro_aluno'),
    
    path('cadastro_admnistrador/', views.cadastro_admnistrador, name='cadastro_admnistrador'),


    path('usuario_update/<int:idusuario>/', views.usuario_update, name='usuario_update'),
    path('usuario_list/', views.usuario_list, name='usuario_list'),  # Certifique-se que essa URL esteja aqui 


    path('cadastro_aluno/', views.cadastro_aluno, name='cadastro_aluno'),
    
    

    
    
     


]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Este arquivo define o mapeamento entre URLs e as views (visualizações) do seu projeto Django. Ele funciona como um roteador, direcionando cada solicitação HTTP para a view correta. O urls.py é organizado em padrões de URL que definem a estrutura das URLs da sua aplicação.

# Ao definir um padrão de URL, você especifica a URL que acionará a view correspondente. A view é a função Python que processa a solicitação e gera a resposta HTML que será enviada ao usuário.