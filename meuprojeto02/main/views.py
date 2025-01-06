from django.shortcuts import render

def index(request):
    return render(request, 'Guia/index.html')

def sobre(request):
    return render(request, 'Sobre/sobre.html')

def teste(request):
    return render(request, 'teste.html')