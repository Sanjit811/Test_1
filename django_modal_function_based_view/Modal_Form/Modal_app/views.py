from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages

# Create your views here.
def home(request):
    stu_obj = Student.objects.all()
    return render(request,'Modal_app/registration.html' ,{'stu':stu_obj})
def add_record(request):
    if request.method == 'POST':
        name = request.POST.get('inst_Name')
        Age = request.POST.get('inst_Age')
        e_mail = request.POST.get('inst_E_mail')
        Password = request.POST.get('inst_Password')
        # print(name,Age,e_mail,Password)

        stu_obj = Student()
        stu_obj.Name = name
        stu_obj.Age = Age
        stu_obj.E_mail = e_mail
        stu_obj.password = Password

        stu_obj.save()
        messages.success(request,'record added Successfully')

        return redirect('add')


def delete_record(request, ID):
    if request.method == 'POST':
        stu_obj = Student.objects.get(pk=ID)
        stu_obj.delete()
        messages.success(request, 'record deleted Successfully')
        return redirect('add')

    else:
        stu_obj = Student.objects.get(pk=ID)
        return redirect(request, 'add', context={'stu':stu_obj})
def update_record(request,ID):
    if request.method == 'POST':
        name = request.POST.get('upd_Name')
        Age = request.POST.get('upd_Age')
        e_mail = request.POST.get('upd_E_mail')
        Password = request.POST.get('upd_Password')
        #print(name,Age,e_mail,Password)
        stu_obj = Student()
        stu_obj.Name = name
        stu_obj.Age = Age
        stu_obj.E_mail = e_mail
        stu_obj.password = Password
        stu_obj.ID = ID

        stu_obj.save()
        messages.success(request, 'record updated Successfully')


        return redirect('add')



    else:
        stu_obj= Student.objects.get(pk=ID)
        return redirect(request,'add', {'stu':stu_obj})