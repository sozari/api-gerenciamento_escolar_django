from django.shortcuts import render

def index(request):
    return render(request, 'Guia/index.html')

def sobre(request):
    return render(request, 'Sobre/sobre.html')

def cadastro_adm(request):
    return render(request, 'Pagina/cadastro_adm.html')

def cadastro_aluno(request):
    return render(request, 'Pagina/cadastro_aluno.html')

def cadastro_professor(request):
    return render(request, 'Pagina/cadastro_profesor.html')

def cadastro_turma(request):
    return render(request, 'Pagina/cadastro_turma.html')

def editar_notas(request):
    return render(request, 'Pagina/editar_notas.html')

def inicial(request):
    return render(request, 'Pagina/inicial.html')

def lista_alunos(request):
    return render(request, 'Pagina/lista_alunos.html')

def login(request):
    return render(request, 'Pagina/login.html')

def turma_select(request):
    return render(request, 'Pagina/turma_select.html')

def turmas_list(request):
    return render(request, 'Pagina/turmas_list.html')

def usuario_list(request):
    return render(request, 'Pagina/usuario_list.html')

def usuario_update(request):
    return render(request, 'Pagina/usuario_update.html')


