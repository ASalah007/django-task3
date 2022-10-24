import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from .models import * 

class StudentsView(View):
    def get(self, req):
        return JsonResponse(serializers.serialize("json", Student.objects.all()), safe=False)

class SubjectsView(View):
    def get(self, req):
        return JsonResponse(serializers.serialize("json", Subject.objects.all()), safe=False)

class ParentsView(View):
    def get(self, req):
        return JsonResponse(serializers.serialize("json", Parent.objects.all()), safe=False)

class ParentView(View):
    def get(self, req, id):
        parent = get_object_or_404(Parent, pk=id)
        return JsonResponse(serializers.serialize("json", [parent]), safe=False)

    def delete(self, req, id):
        parent = get_object_or_404(Parent, pk=id)
        parent.delete()
        return HttpResponse("Deleted")


class StudentView(View):
    def get(self, req, id):
        pass

    def delete(self, req, id):
        student = get_object_or_404(Student, pk=id)
        student.delete()
        return HttpResponse("Deleted")


class SubjectView(View):
    def get(self, req, id):
        pass

    def delete(self, req, id):
        subject = get_object_or_404(Subject, pk=id)
        subject.delete()
        return HttpResponse("Deleted")
