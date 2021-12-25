from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from greenCircle.models import Category, Trainer, CourseRequest, Course
from django.core.paginator import Paginator
from . import forms


def greenCircle(request):
    cats = Category.objects.all()
    context = {"cats": cats}
    return render(request, 'greenCircle/greenCircle.html', context)


def greenCircleCourses(request, pk):
    courses = Course.objects.filter(category_id=pk)
    context = {"courses": courses}
    return render(request, 'greenCircle/greencourses.html', context=context)


def green_trainer_details(request, pk):
    trainer = Trainer.objects.get(courses=pk)
    context = {"trainer": trainer}
    return render(request, 'greenCircle/greentrainer.html', context=context)


class CourseRequestView(View):
    def get(self, request, pk):
        form = forms.CourseRequestForm()
        course = Course.objects.get(pk=pk)
        context = {"course": course, "form": form}
        return render(request, 'greenCircle/greencourse_request.html', context)

    def post(self, request, pk):
        form = forms.CourseRequestForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")
            obj = CourseRequest.objects.create(name=name, phone=phone, course_id=pk, email=email)
            obj.save()
            return redirect('green-circle')
        else:
            return JsonResponse({"message": "bad data"})


def add_greenCourse(request):
    trainer = Trainer.objects.all()
    category = Category.objects.all()
    if request.method == 'POST' and request.FILES['logo']:
        name = request.POST.get('name')
        description = request.POST.get('description')
        start = request.POST.get('start')
        end = request.POST.get('end')
        trainer = request.POST.get('trainer')
        total = request.POST.get('total_hour')
        category = request.POST.get('cat')
        link = request.POST.get('link')
        logo = request.FILES['logo']
        fs = FileSystemStorage()
        fs.save(logo.name, logo)
        course = Course(name=name, description=description, logo=logo, link=link, duration=total, category_id=category,
                        trainer_id=trainer, start_date=start, end_date=end)
        course.save()
        if course.pk:
            return redirect('user-profile-dash')
    return render(request, 'greenCircle/add-greenCircle.html', context={"cats": category, "trainers": trainer})


def Greencourses_list(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"courses": page_obj}
    return render(request, 'greenCircle/greenCircleList.html', context)


def Greenrequest_list(request):
    requests = CourseRequest.objects.all()
    paginator = Paginator(requests, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"courses": page_obj}
    return render(request, 'greenCircle/greenRequestList.html', context)


def Greentrainers_list(request):
    trainers = Trainer.objects.all()
    paginator = Paginator(trainers, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"trainers":page_obj}
    return render(request, 'greenCircle/green_trainerList.html', context)
