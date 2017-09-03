from django.shortcuts import render
from django.http import HttpResponse
from basicapp.forms import FormMessage
# Create your views here.


def index(request):
    return render(request,'index.html')

def form_name_view(request):
    form = FormMessage()

    if request.method == "POST":
        form = FormMessage(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('error')           
    return render(request,'message.html',{'form':form})