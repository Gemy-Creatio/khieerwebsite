from django.shortcuts import render
from greenCircle.models import Category, Trainer, CourseRequest, Course


def greenCircle(request):
    context = {"cats": Category.objects.all()}
    return render(request, 'greenCircle/greenCircle.html', context)
