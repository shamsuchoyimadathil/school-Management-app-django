from django.urls import path

from . import views

urlpatterns = [
    #path("",views.StudentsInfo.as_view(),name="students-info"),
    path("",views.students_info,name="students"),
    path("add-student",views.AddStudent.as_view(),name="add-student") ,
    path("edit-student/<slug:slug>",views.EditStudent.as_view(),name="edit-student"),
    path("delete-student/<slug:slug>",views.delete_student,name="delete-student")
]

