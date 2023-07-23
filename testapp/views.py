from django.shortcuts import render , redirect
from testapp.models import Emp_model
from testapp.forms import EmloyeeForm
# Create your views here.
def retrive_view(request):
    emp_list=Emp_model.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})
def Inser_view(request):
    form=EmloyeeForm()
    if request.method == 'POST':
        form=EmloyeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        
    return render(request,'testapp/insert.html',{'form':form})
def delete_view(request,id):
    employee=Emp_model.objects.get(id=id)
    employee.delete()
    return redirect('/')
def update_view(request,id):
    employee=Emp_model.objects.get(id=id)
    form=EmloyeeForm(instance=employee)
    if request.method=='POST':
        form=EmloyeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/')


    return render(request,'testapp/update.html',{'form':form})

