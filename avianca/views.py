from django.shortcuts import render, redirect
from .models import Vuelo
from .forms import FormVuelo

# Create your views here.


def hogar(request):
    return render(request, 'hogar.html')


def registrar(request):
    if request.method == 'POST':
        form = FormVuelo(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar')  
    else:
        form = FormVuelo()
    return render(request, 'registrar.html', {'form': form})


def listar(request):
    return render(request, 'listar.html', {'flights': Vuelo.objects.all().order_by('price')})


def estadisticas(request):
    return render(request, 'estadisticas.html', {None})