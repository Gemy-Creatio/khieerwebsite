from django.shortcuts import render
from greenCircle.models import Category, Trainer, CourseRequest, Course


def greenCircle(request):
    context = {"cats": Category.objects.all()}
    return render(request, 'greenCircle/greenCircle.html', context)


def greenCircleCourses(request, pk):
    context = {"courses": Course.objects.filter(category_id=pk)}
    return render(request, 'greenCircle/greencourses.html', context=context)


def green_trainer_details(request, pk):
    context = {"trainer": Trainer.objects.get(course=pk)}
    return render(request, 'greenCircle/greentrainer.html', context=context)
