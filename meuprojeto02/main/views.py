from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect  # Usado para redirecionar o usuário para uma nova URL
from django.shortcuts import render, redirect  # 'render' para renderizar templates e 'redirect' para redirecionar o usuário
from main.bd_config import conecta_no_banco_de_dados  # Função personalizada para conectar-se ao banco de dados
# from .forms import ContatoForm  # Importa o formulário personalizado 'ContatoForm' para manipulação de dados do usuário
from django.shortcuts import render  # Usado para renderizar templates HTML com dados contextuais
from django.contrib.auth import authenticate, login, logout  # Funções de autenticação para autenticar, logar e deslogar usuários
from django.contrib.auth.models import User  # Modelo de usuário padrão do Django, para criação e manipulação de usuários
#from django.contrib.auth.decorators import login_required  # Para proteger views que exigem um usuário autenticado (comentado)
from django.views.decorators.csrf import csrf_protect  # Ativa a proteção CSRF para uma view específica
from django.contrib.auth.decorators import login_required  # Decorator que exige que o usuário esteja autenticado para acessar a view
from django.contrib.auth.mixins import LoginRequiredMixin  # Mixin para garantir que apenas usuários autenticados acessem views baseadas em classe
from django.shortcuts import render, redirect  # 'render' para templates e 'redirect' para redirecionamentos de URL
from django.http import HttpResponseBadRequest  # Retorna uma resposta HTTP com erro 400 (Bad Request)
from django.db import transaction  # Usado para controlar transações de banco de dados (commit/rollback)
from django.http import HttpResponse, JsonResponse  # 'HttpResponse' para resposta genérica e 'JsonResponse' para respostas JSON
from django.contrib import messages  # Usado para mostrar mensagens de feedback ao usuário, como sucesso ou erro


from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm




from django.contrib.auth.hashers import make_password
import mysql.connector



from django.http import JsonResponse
from django.db import connection


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




# Função para exibir o formulário de cadastro de turma
def mostrar_formulario_turma(request):
    with connection.cursor() as cursor:
        # Obtém a lista de professores
        cursor.execute("SELECT idusuario, nome FROM usuarios WHERE tipo_usuario = 'professor'")
        professores = cursor.fetchall()

    # Renderiza o template e envia a lista de professores
    return render(request, 'cadastro_turma.html', {'professores': professores})

# Função para processar o formulário via POST
@csrf_exempt
def cadastro_formulario_turma(request):
    if request.method == 'POST':
        nome_turma = request.POST.get('nome_turma')
        idprofessor = request.POST.get('idprofessor')

        # Validando os campos
        if not nome_turma or not idprofessor:
            return JsonResponse({'mensagem': 'Todos os campos são obrigatórios!'}, status=400)

        # Preparando a query para inserir a turma
        sql_turma = "INSERT INTO turmas (nome_turma, idusuario) VALUES (%s, %s)"
        print(f"Valores para inserção: nome_turma = {nome_turma}, idprofessor = {idprofessor}")

        try:
            # Executando a query no banco de dados
            with connection.cursor() as cursor:
                cursor.execute(sql_turma, [nome_turma, idprofessor])

            return redirect('/turmas/cadastro/')  # Redireciona de volta para o formulário

        except Exception as error:
            print(f"Erro ao cadastrar turma: {error}")
            return JsonResponse({'error': f'Erro ao processar os dados: {str(error)}'}, status=500)

    return JsonResponse({'mensagem': 'Método não permitido!'}, status=405)




def listar_usuarios(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idusuario, nome, email, tipo_usuario FROM usuarios")
            usuarios = cursor.fetchall()

        # Criando a lista de usuários para enviar como resposta JSON
        usuarios_list = [
            {'idusuario': idusuario, 'nome': nome, 'email': email, 'tipo_usuario': tipo_usuario}
            for idusuario, nome, email, tipo_usuario in usuarios
        ]

        return JsonResponse(usuarios_list, safe=False)
    
    except Exception as e:
        return JsonResponse({'error': f'Erro ao listar os usuários: {str(e)}'}, status=500)



def listar_usuarios_html(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idusuario, nome, email, tipo_usuario FROM usuarios")
            usuarios = cursor.fetchall()

        return render(request, 'Pagina/usuario_list.html', {'usuarios': usuarios})

    except Exception as e:
        return JsonResponse({'error': f'Erro ao listar os usuários: {str(e)}'}, status=500)


def mostrar_formulario_aluno(request):
    try:
        with connect_to_database().cursor() as cursor:
            cursor.execute("SELECT idturma, nome_turma FROM turmas")
            turmas = cursor.fetchall()
        return render(request, 'Pagina/cadastro_aluno.html', {'turmas': turmas})
    except Exception as error:
        print(f"Erro ao carregar o formulário: {error}")
        return JsonResponse({'error': f"Erro ao carregar o formulário: {str(error)}"}, status=500)
def cadastro_formulario_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        telefone_responsavel = request.POST.get('telefone_responsavel')
        idturma = request.POST.get('idturma')

        if not all([nome, email, senha, telefone_responsavel, idturma]):
            return JsonResponse({'mensagem': 'Todos os campos são obrigatórios!'}, status=400)

        senha_hash = make_password(senha)

        sql_usuario = "INSERT INTO usuarios (nome, email, senha, tipo_usuario) VALUES (%s, %s, %s, 'aluno')"
        sql_aluno = "INSERT INTO aluno (idusuario, telefone_responsavel, idturma) VALUES (%s, %s, %s)"
        sql_notas = "INSERT INTO notas (idusuario, idturma) VALUES (%s, %s)"

        try:
            with connect_to_database().cursor() as cursor:
                cursor.execute(sql_usuario, [nome, email, senha_hash])
                idusuario = cursor.lastrowid

                cursor.execute(sql_aluno, [idusuario, telefone_responsavel, idturma])
                cursor.execute(sql_notas, [idusuario, idturma])

            return redirect('mostrar_formulario')
        except Exception as error:
            print(f"Erro no banco de dados: {error}")
            return JsonResponse({'error': f"Erro ao cadastrar aluno: {str(error)}"}, status=500)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    
def mostrar_formulario_professor(request):
    return render(request, 'cadastro_professor.html')

def cadastro_formulario_professor(request):
    if request.method == 'POST':
        # Capturando os dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        telefone = request.POST.get('telefone')

        # Validando campos obrigatórios
        if not nome or not email or not senha or not telefone:
            return JsonResponse({'mensagem': 'Todos os campos são obrigatórios!'}, status=400)

        # Criptografando a senha
        senha_hash = make_password(senha)

        # Preparando as queries SQL
        sql_usuario = "INSERT INTO usuarios (nome, email, senha, tipo_usuario) VALUES (%s, %s, %s, %s)"
        sql_professor = "INSERT INTO professor (idusuario, telefone) VALUES (%s, %s)"

        try:
            with connection.cursor() as cursor:
                # Inserindo usuário na tabela 'usuarios'
                cursor.execute(sql_usuario, [nome, email, senha_hash, 'professor'])
                idusuario = cursor.lastrowid  # Obtendo o ID gerado

                # Inserindo na tabela 'professor' com o ID gerado
                cursor.execute(sql_professor, [idusuario, telefone])

                # Commitando a transação
                connection.commit()

            # Após o cadastro, redireciona para o formulário novamente
            return redirect('professor_cadastro')  # Redireciona para a página de cadastro

        except Exception as error:
            return JsonResponse({'error': f'Erro ao processar os dados: {str(error)}'}, status=500)
    
def mostrar_formulario_turma(request):
        # Obtém a lista de usuários do tipo 'professor' da tabela 'usuarios'
    with connect_to_database() as mydb:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT idusuario, nome FROM usuarios WHERE tipo_usuario = 'professor'")
        professores = mycursor.fetchall()
def cadastro_formulario_turma(request):
        if request.method == 'POST':
            nome_turma = request.POST['nome_turma']
            idprofessor = request.POST['idprofessor']

        # Validando os campos
        if not nome_turma or not idprofessor:
            return JsonResponse({'mensagem': 'Todos os campos são obrigatórios!'}, status=400)

        # Preparando a query para inserir a turma
        sql_turma = "INSERT INTO turmas (nome_turma, idusuario) VALUES (%s, %s)"
        
        print(f"Valores para inserção: nome_turma = {nome_turma}, idprofessor = {idprofessor}")  # Logando os dados antes de executar a query

        try:
            # Conectando ao banco de dados
            with connect_to_database() as mydb:
                mycursor = mydb.cursor()
                mycursor.execute(sql_turma, (nome_turma, idprofessor))
                mydb.commit()

            return redirect(reverse('mostrar_formulario'))  # Redireciona de volta após o cadastro

        except mysql.connector.Error as error:
            print(f"Erro ao cadastrar turma: {error}")  # Adicionando print do erro
            return JsonResponse({'error': f'Erro ao processar os dados: {str(error)}'}, status=500)
        else:
            return JsonResponse({'mensagem': 'Método não permitido'}, status=405)

def mostrar_formulario_adm(request):
    return render(request, 'cadastro_adm.html')

def cadastro_formulario_adm(request):
    if request.method == 'POST':
        # Capturando os dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Validando campos obrigatórios
        if not nome or not email or not senha:
            return JsonResponse({'mensagem': 'Todos os campos são obrigatórios!'}, status=400)

        # Criptografando a senha
        senha_hash = make_password(senha)

        # Preparando a query SQL
        sql_usuario = "INSERT INTO usuarios (nome, email, senha, tipo_usuario) VALUES (%s, %s, %s, %s)"

        try:
            with connection.cursor() as cursor:
                # Inserindo usuário na tabela 'usuarios'
                cursor.execute(sql_usuario, [nome, email, senha_hash, 'administrador'])
                connection.commit()

            # Após o cadastro, redireciona para o formulário novamente
            return redirect('adm_cadastro')  # Redireciona para a página de cadastro

        except Exception as error:
            return JsonResponse({'error': f'Erro ao processar os dados: {str(error)}'}, status=500)
        
def usuario_list(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idusuario, nome, email, tipo_usuario FROM usuarios")
            usuarios = cursor.fetchall()

        # Verifica se a requisição é AJAX verificando o cabeçalho 'X-Requested-With'
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse([
                {'idusuario': idusuario, 'nome': nome, 'email': email, 'tipo_usuario': tipo_usuario}
                for idusuario, nome, email, tipo_usuario in usuarios
            ], safe=False)
        else:
            # Para requisição normal, renderiza a página HTML
            return render(request, 'Pagina/usuario_list.html', {'usuarios': usuarios})

    except Exception as e:
        return JsonResponse({'error': f'Erro ao listar os usuários: {str(e)}'}, status=500)













        
        
        
        
        
        
        
        
        
        
        
        
        
def usuario_listagem(request):
    usuarios = Usuario.objects.all()  # Recupera todos os usuários
    return render(request, 'usuario_listagem.html', {'usuarios': usuarios})


def usuario_edit(request, idusuario):
    usuario = get_object_or_404(Usuario, id=idusuario)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_listagem')  # Redireciona para a lista de usuários
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'usuario_edit.html', {'form': form, 'usuario': usuario})



def usuario_delete(request, idusuario):
    usuario = get_object_or_404(Usuario, id=idusuario)
    usuario.delete()
    return redirect('usuario_listagem')  # Redireciona para a lista de usuários













def excluirusuario(request, id):
    try:
        # Estabelecer conexão com o banco de dados
        bd = conecta_no_banco_de_dados()
        cursor = bd.cursor()

        # Exclusão de dependências relacionadas ao usuário
        cursor.execute("DELETE FROM aluno WHERE idusuario = %s", (id,))
        cursor.execute("DELETE FROM professor WHERE idusuario = %s", (id,))

        # Exclusão do usuário principal
        cursor.execute("DELETE FROM usuarios WHERE idusuario = %s", (id,))
        bd.commit()

        if cursor.rowcount == 0:
            # Caso nenhum registro seja afetado, significa que o ID não foi encontrado
            messages.error(request, 'Nenhum usuário encontrado com este ID.')
            return redirect('/usuario_list/')

        messages.success(request, 'Usuário excluído com sucesso!')
        return redirect('/usuario_list/')

    except Exception as e:
        print(f"Erro ao excluir usuário: {e}")
        messages.error(request, 'Falha ao excluir usuário. Tente novamente mais tarde.')
        return redirect('/usuario_list/')  # Redireciona mesmo em caso de erro

    finally:
        # Fechando conexão com o banco
        cursor.close()
        bd.close()





    
    
    

    
    
    













# View para exibir o formulário de cadastro de professor
def mostrar_formulario_professor(request):
    return render(request, 'cadastro_professor.html')

# View para processar os dados do formulário de cadastro de professor
def submit_formulario_professor(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Validando campos obrigatórios
        if not nome or not email or not senha:
            messages.error(request, "Todos os campos são obrigatórios!")
            return redirect('cadastro_professor')  # Redireciona de volta para o formulário

        # Criptografando a senha
        senha_hash = make_password(senha)

        # Salvando o novo professor
        try:
            Usuario.objects.create(nome=nome, email=email, senha=senha_hash, tipo_usuario='professor')
            messages.success(request, "Professor cadastrado com sucesso!")
            return redirect('cadastro_professor')  # Redireciona para o formulário após sucesso
        except Exception as e:
            messages.error(request, f"Erro ao processar o cadastro: {str(e)}")
            return redirect('cadastro_professor')  # Redireciona para o formulário em caso de erro
        
        
        
        
        
        # Cadastro de Administrador
def mostrar_formulario_adm(request):
    return render(request, 'cadastro_adm.html')

def submit_formulario_adm(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Validando campos obrigatórios
        if not nome or not email or not senha:
            messages.error(request, "Todos os campos são obrigatórios!")
            return redirect('cadastro_adm')  # Redireciona de volta para o formulário

        # Criptografando a senha
        senha_hash = make_password(senha)

        # Salvando o novo administrador
        try:
            Usuario.objects.create(nome=nome, email=email, senha=senha_hash, tipo_usuario='administrador')
            messages.success(request, "Administrador cadastrado com sucesso!")
            return redirect('cadastro_adm')  # Redireciona para o formulário após sucesso
        except Exception as e:
            messages.error(request, f"Erro ao processar o cadastro: {str(e)}")
            return redirect('cadastro_adm')  # Redireciona para o formulário em caso de erro
        
        
        
        # Cadastro de Aluno
def mostrar_formulario_aluno(request):
    return render(request, 'cadastro_aluno.html')

def submit_formulario_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Validando campos obrigatórios
        if not nome or not email or not senha:
            messages.error(request, "Todos os campos são obrigatórios!")
            return redirect('cadastro_aluno')  # Redireciona de volta para o formulário

        # Criptografando a senha
        senha_hash = make_password(senha)

        # Salvando o novo aluno
        try:
            Usuario.objects.create(nome=nome, email=email, senha=senha_hash, tipo_usuario='aluno')
            messages.success(request, "Aluno cadastrado com sucesso!")
            return redirect('cadastro_aluno')  # Redireciona para o formulário após sucesso
        except Exception as e:
            messages.error(request, f"Erro ao processar o cadastro: {str(e)}")
            return redirect('cadastro_aluno')  # Redireciona para o formulário em caso de erro
        
        
        
        
def cadastro_admnistrador(request):
    #if not request.session.get('usuario_id'):
     #   return redirect('/')
    #else:
        if request.method == 'POST':
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')

            # Valide a entrada (assumindo lógica de validação)
            if not all([nome, email, senha]):
                # Lide com erros de validação (por exemplo, exiba mensagens de erro)
                return render(request, '/cadastro_adm.html/')

            # Criptografando a senha
            senha_hash = make_password(senha)

            # Atualize os dados do usuário se a validação for aprovada
            bd = conecta_no_banco_de_dados()
            cursor = bd.cursor()
            sql = (
                """
                INSERT INTO usuarios
                SET nome = %s, email = %s, senha = %s, tipo_usuario = %s;
                """
            )
            values = (nome, email, senha_hash, 'administrador')
            cursor.execute(sql, values)
            bd.commit()  
            cursor.close()
            bd.close()

            # Redirecione para a página de sucesso ou exiba a mensagem de confirmação
            messages.success(request, "Administrador cadastrado com sucesso!")
            return redirect('cadastro_adm')  # Aqui o nome da URL

        # Exiba o formulário (caso não seja POST)
        return render(request, '/cadastro_adm.html/')
    
    
    
    
    
    





def usuario_update(request, idusuario):
    if request.method == "GET":
        # Consultar o usuário pelo ID
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE idusuario = %s", [idusuario])
            usuario = cursor.fetchone()

        if usuario:
            return render(request, 'Pagina/usuario_update.html', {'usuario': usuario})
        else:
            return redirect('usuario_list')

    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Atualizar o usuário no banco de dados
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE idusuario = %s",
                [nome, email, senha, idusuario]  # Usando idusuario para atualizar corretamente
            )

        return redirect('usuario_list')




def cadastro_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        telefone_responsavel = request.POST.get('telefone_responsavel')
        idturma = request.POST.get('idturma')

        if not all([nome, email, senha, telefone_responsavel, idturma]):
            messages.error(request, 'Todos os campos são obrigatórios.')
            return redirect('cadastro_aluno')

        senha_hash = make_password(senha)

        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO usuarios (nome, email, senha, tipo_usuario)
                VALUES (%s, %s, %s, %s)
                """,
                [nome, email, senha_hash, 'aluno']
            )
            idusuario = cursor.lastrowid
            cursor.execute(
                """
                INSERT INTO aluno (idusuario, telefone_responsavel, idturma)
                VALUES (%s, %s, %s)
                """,
                [idusuario, telefone_responsavel, idturma]
            )
            cursor.execute(
                """
                INSERT INTO notas (idusuario, idturma)
                VALUES (%s, %s)
                """,
                [idusuario, idturma]
            )
            connection.commit()

        messages.success(request, 'Aluno cadastrado com sucesso!')
        return redirect('cadastro_aluno')

    with connection.cursor() as cursor:
        cursor.execute("SELECT idturma, nome_turma FROM turmas")
        turmas = cursor.fetchall()

    return render(request, 'Pagina/cadastro_aluno.html', {'turmas': turmas})



