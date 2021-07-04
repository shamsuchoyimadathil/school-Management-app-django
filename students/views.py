from django.shortcuts import render , HttpResponseRedirect , get_object_or_404
from django.views.generic.base import TemplateView, View
from django.http.response import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView , DeleteView

from . forms import StudentForm
from . models import Student


# Create your views here.

# class StudentsInfo(ListView):
#     template_name = "students_info/students-info.html"
#     model = Student
#     context_object_name = "students_info"

def students_info(request):
    #latest_post = Student.objects.all().order_by["-id"]
    latest_post = Student.objects.all()
    form = StudentForm
    return render(request,"students_info/students-info.html" ,{
        "latest_post":latest_post,
        "form":form
    })


class AddStudent(View):

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


class EditStudent(UpdateView):
    template_name = "add_student/add-student.html"
    model = Student
    fields = [
        "first_name",
        "last_name",
        "DOB",
        "gender",
        "address_line_1",
        "address_line_2",
        "city",
        "zipcode"
    ]
    success_url = "/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["check_variable"] = True
        return context


# class DeleteStudent(DeleteView):
#     #template_name = "delete_student/delete-student.html"
#     template_name = "students_info/students-info.html"
#     #template_name = "main_page/main-page.html"
#     model = Student
#     success_url = "/"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context ["has_delete"] = True
#         return context

#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


def delete_student(request,slug):
    context = {}
    obj = get_object_or_404(Student,slug=slug)

    if request.method =="POST":
        print(obj)
        obj.delete()
        return HttpResponseRedirect ("/")

    return render(request,"delete_student/delete-student.html",context)