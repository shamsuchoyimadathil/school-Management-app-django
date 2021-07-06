from django.shortcuts import render , HttpResponseRedirect , get_object_or_404
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import UpdateView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from . forms import StudentForm
from . models import Student

@login_required(login_url="/accounts/login/")
def students_info(request):
    latest_post = Student.objects.all()
    form = StudentForm
    return render(request,"students_info/students-info.html" ,{
        "latest_post":latest_post,
        "form":form
    })


class AddStudent(LoginRequiredMixin,View):

    def get(self,request):
        form = StudentForm
        return render(request,"add_student/add-student.html",{
            "form":form
        })

    def post(self,request):
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

        return render(request,"add_student/add-student.html",{
            "form":form
        })


class EditStudent(LoginRequiredMixin,UpdateView):
    template_name = "add_student/add-student.html"
    model = Student
    form_class = StudentForm
    success_url = "/"


@login_required(login_url="/accounts/login/")
def delete_student(request,slug):
    context = {}
    obj = get_object_or_404(Student,slug=slug)

    if request.method =="POST":
        print(obj)
        obj.delete()
        return HttpResponseRedirect ("/students-sec/")

    return render(request,"delete_student/delete-student.html",context)