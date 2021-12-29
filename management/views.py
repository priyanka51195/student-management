from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from management.models import Entry
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.


def register(request):
    return render(request, 'management.html')

def show(request):
    data = Entry.objects.all()
    return render(request , 'show.html', {'data': data})

def send(request):
     if request.method =='POST':
         ID =request.POST.get('id')
         name =request.POST['name']
         address = request.POST['address']
         number = request.POST['number']
         password = request.POST['password']
         Entry(ID=ID ,name=name,address=address,number=number,password= password).save()
         msg = "Data stored successfully "
         return render(request,'management.html', {'msg' : msg})
     else:
         return HttpResponse("<h1> Please fill the correct data</h1>" )


def delete(request):
    ID = request.GET['id']
    Entry.objects.filter(ID =ID).delete()
    return HttpResponseRedirect ("show")


def edit(request):
    ID = request.GET.get('id')
    name=address = number = password = "not available"
    for data in Entry.objects.filter(ID = ID):
        name= data.name
        address = data.address
        number = data.number
        password = data.password
    return render(request, "edit.html" ,{'ID':ID, 'name': name ,'address': address,'number': number,'password': password })

def RecordEdited(request):
    if request.method == 'POST':
        ID = request.POST['ID']
        name = request.POST['name']
        address = request.POST['address']
        number = request.POST['number']
        password = request.POST['password']
        Entry.objects.filter(ID=ID).update(name=name, address= address, number=number, password=password)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1> Please fill the correct data</h1>")



# Create your views here.
