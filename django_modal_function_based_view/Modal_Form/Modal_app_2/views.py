from django.shortcuts import render, redirect
from . models import Student
from django.contrib import messages

# Create your views here.
def refreshlist():
    stu_obj = Student.objects.all()
    return {'stu': stu_obj}
def home(request):
    context = refreshlist()


    return render(request, template_name='Modal_app_2/registration.html', context=context)

def add_record(request):
    if request.method == 'POST':
        name=request.POST.get('inst_Name')
        age = request.POST.get('inst_Age')
        e_mail = request.POST.get('inst_E_mail')
        password = request.POST.get('inst_Password')
        #print(name,age,e_mail,password)

        stu_obj=Student()
        stu_obj.Name=name
        stu_obj.Age=age
        stu_obj.E_mail=e_mail
        stu_obj.password=password
        stu_obj.save()
        messages.success(request, 'record added Successfully')
        return redirect('app_addrecord')
        #messages.success(request, 'record added Successfully')
        #messages.success(request, 'record added Successfully')

    return render(request, template_name='Modal_app_2/insertForm.html')


def update_record(request, id):
    if request.method == 'POST':
        name = request.POST.get('upd_Name')
        age = request.POST.get('upd_Age')
        e_mail = request.POST.get('upd_E_mail')
        password = request.POST.get('upd_Password')
        #print(name,age,e_mail,password)

        stu_obj = Student()
        stu_obj.Name = name
        stu_obj.Age = age
        stu_obj.E_mail = e_mail
        stu_obj.password = password
        stu_obj.ID = id
        stu_obj.save()
        messages.success(request, 'record updated Successfully')
        return redirect('App_home')
    else:
        stu_obj = Student.objects.get(pk=id)
        context = {'stu': stu_obj}
        return render(request, template_name='Modal_app_2/updateForm.html', context=context )

def delete_record(request, id):
    if request.method == 'POST':
        stu_obj=Student.objects.get(pk=id)
        stu_obj.delete()
        messages.success(request, 'record deleted Successfully')
        return redirect('App_home')

    else:
        stu_obj = Student.objects.get(pk=id)
        context={'stu': stu_obj}
        return redirect(request, 'App_home', context=context)


