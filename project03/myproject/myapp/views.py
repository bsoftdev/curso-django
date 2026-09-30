from django.contrib import messages
from django.shortcuts import render, redirect
from myapp.models import Client

# Create your views here.

#VIEW PARA MOSTAR A TELA HOME
def home_view(request):
    return render(request, 'clients/home.html')


#VIEW PARA CADASTRAR CLIENTES
def cadastrar(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name!= '' and email != '':
            Client.objects.create(name_client = name, email = email)
            messages.success(request, 'Cliente cadastrado com sucesso')
            return redirect('clientes')

    return render(request, "clients/cadastro.html")



#VIEW PARA MOSTRAR TODOS CLIENTES
def  show_clients(request):
    clientes = Client.objects.all()
    return render(request, 'clients/lista_clients.html', {'clients':clientes})


#VIEW PARA DELETAR CLIENTE
def delete(request, client_id):

    client = Client.objects.get(id = client_id)

    if request.method == 'POST':

        client.delete()
        messages.success(request, 'Cliente eliminado  com sucesso')
        return redirect('clientes')
        
    return render(request, 'clients/confirm_delete.html', {'client':client})



def editar(request, client_id):

    client = Client.objects.get(id = client_id)

    if request.method == 'POST':
        if client:
            
            client.name_client = request.POST.get('name')
            client.email = request.POST.get('email')
            client.save()
            return redirect('clientes')

    return render(request, 'clients/editar_form.html', {'client':client})