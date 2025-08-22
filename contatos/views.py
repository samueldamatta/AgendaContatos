from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contato
from .forms import ContatoForm
import csv

# Create your views here.
def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/lista_contatos.html', {'contatos': contatos})

def novo_contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contatos/novo_contato.html', {'form': ContatoForm(), 'sucesso': True})
    else:
        form = ContatoForm()
    return render(request, 'contatos/novo_contato.html', {'form': form})

def editar_contato(request, id):
    contato = Contato.objects.get(id=id)
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('lista_contatos')
    else:
        form = ContatoForm(instance=contato)
    return render(request, 'contatos/editar_contato.html', {'form': form, 'contato': contato})

def deletar_contato(request, id):
    contato = Contato.objects.get(id=id)
    if request.method == "POST":
        contato.delete()
        return redirect('lista_contatos')
    return render(request, 'contatos/deletar_contato.html', {'contato': contato})

def exportar_csv(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="contatos.csv"'
    response.write('\ufeff')
    writer = csv.writer(response)
    writer.writerow(['Nome', 'Telefone', 'Email'])
    contatos = Contato.objects.all()
    for contato in contatos:
        writer.writerow([contato.nome, contato.telefone, contato.email])
    
    return response