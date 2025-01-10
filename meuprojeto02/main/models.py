from django.db import models

# Create your models here.



class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=50)  # Ex.: 'admin', 'professor', 'aluno'
    
    class Meta:
        db_table = 'usuarios'  # Nome da tabela no banco de dados

    def __str__(self):
        return self.nome


from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    mensagem = models.TextField()
