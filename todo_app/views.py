from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from todo_app.models import backend
from todo_app.models import deneme

# Create your views here.
def index(request):
    return HttpResponse("index sayfam")
def deneme(request):
    return render(request,"todo_app/abaut.html",{"merhaba":"deneme"})
def anaSayfa(request):
    return render(request,"todo_app/index.html")
def main(request):
    return render(request,"todo_app/base.html")
def ndviolustur(request):
    context = {}
    name=""
    if request.method =="POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        url= fs.url(name)
        context["url"]=fs.url(name)
        print(name)
    return render(request,"todo_app/ndviolustur.html",context)
def ndvihesaplama(request):
    resim="media/images/ndviresim.tif"
    return render(request,"todo_app/ndvihesaplama.html",{"merhaba":resim},backend().badana())






