from django import forms
from .models import Contato,Usuario




class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'tipo_usuario']

    # Customizando o estilo dos campos (opcional)
    nome = forms.CharField(
        label="Nome",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o email'})
    )
    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a senha'})
    )
    tipo_usuario = forms.CharField(
        label="Tipo de Usuário",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: admin, professor, aluno'})
    )






















class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'senha'] 
  
    email = forms.EmailField(
        label='Email', 
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email', 'class':'inputlogin'})
    )
    senha = forms.CharField(
        label='Senha', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha', 'class':'inputlogin'})
    )
    
    
    
    