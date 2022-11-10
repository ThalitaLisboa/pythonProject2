from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
from .entidades import cliente
from .services import cliente_service
# Create your views here.


# vai retornar a lista de clientes
def listar_clientes(request):   # request: objeto que vai ter todas os parametros da requisição
    #clientes = Cliente.objects.all()  #faz um select na db e devolve tudo da tabela. utilizando a orm do django
    clientes = cliente_service.listar_clientes()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})  #obtem a lista de clientes e devolve atarves da variavel clientes


# metodo para inserir
def inserir_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            #form.save()
            nome = form.cleaned_data["nome"]
            sexo = form.cleaned_data["sexo"]
            data_nascimento = form.cleaned_data["data_nascimento"]
            email = form.cleaned_data["email"]
            profissao = form.cleaned_data["profissao"]
            cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, data_nascimento=data_nascimento,
                                           email=email, profissao=profissao)
            cliente_service.cadastrar_cliente(cliente_novo)
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/form_cliente.html', {'form': form})


#buscar cliente por id
def listar_cliente_id(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    return render(request, 'clientes/lista_cliente.html', {'cliente': cliente})


# metodo para editar
def editar_cliente(request, id):
    cliente_antigo = cliente_service.listar_cliente_id(id)
    form = ClienteForm(request.POST or None, instance=cliente_antigo)  #com base nos dados que já foi preenchido ou a instacia do formulario estará em branco
    if form.is_valid():
        #form.save()
        nome = form.cleaned_data["nome"]
        sexo = form.cleaned_data["sexo"]
        data_nascimento = form.cleaned_data["data_nascimento"]
        email = form.cleaned_data["email"]
        profissao = form.cleaned_data["profissao"]
        cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, data_nascimento=data_nascimento,
                                       email=email, profissao=profissao)
        cliente_service.editar_cliente(cliente_antigo, cliente_novo)
        return redirect('listar_clientes')
    return render(request, 'clientes/form_cliente.html', {'form': form})



#metodo para remover um cliente
def remover_cliente(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    if request.method == "POST":
        cliente_service.remover_cliente(cliente)
        return redirect('listar_clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente})