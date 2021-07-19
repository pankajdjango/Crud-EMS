from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import EmsForm
from .models import Ems
# Create your views here.
def index(request):
    if request.method=='POST':
        form=EmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=EmsForm()
    alldata=Ems.objects.all()
    return render(request,'index.html',{'form':form,'data':alldata})

def update(request,id):
    if request.method=='POST':
        data=Ems.objects.get(pk=id)
        form=EmsForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        data = Ems.objects.get(pk=id)
        form = EmsForm(instance=data)
    return render(request,'edit.html',{'form':form})

def delete(request,id):
    if request.method == 'POST':
        pi = Ems.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')