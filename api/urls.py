from django.urls import path
from .views import * 

urlpatterns = [
    path("students/", StudentsView.as_view()),
    path("subjects/", SubjectsView.as_view()),
    path("parents/", ParentsView.as_view()),
    path("students/<int:id>/", StudentView.as_view()),
    path("parents/<int:id>/", ParentView.as_view()),
    path("Subjects/<int:id>/", SubjectView.as_view())
]
