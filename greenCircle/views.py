from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from greenCircle.models import Category, Trainer, CourseRequest, Course


def greenCircle(request):
    context = {"cats": Category.objects.all()}
    return render(request, 'greenCircle/greenCircle.html', context)


def greenCircleCourses(request, pk):
    context = {"courses": Course.objects.filter(category_id=pk)}
    return render(request, 'greenCircle/greencourses.html', context=context)


def green_trainer_details(request, pk):
    context = {"trainer": Trainer.objects.get(courses=pk)}
    return render(request, 'greenCircle/greentrainer.html', context=context)


def course_request(request, pk):
    course = Course.objects.get(pk=pk)
    context = {"course": course}
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        course_obj = CourseRequest(name=name, phone=phone, email=email, course=course)
        course_obj.save()
        if course_obj.pk:
            return redirect('green-circle', course.category.id)
    return render(request, 'greenCircle/greencourse_request.html', context)


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
    context = {"courses": Course.objects.all()}
    return render(request, 'greenCircle/greenCircleList.html', context)


def Greenrequest_list(request):
    context = {"courses": CourseRequest.objects.all()}
    return render(request, 'greenCircle/greenRequestList.html', context)


def Greentrainers_list(request):
    context = {"trainers": Trainer.objects.all()}
    return render(request, 'greenCircle/green_trainerList.html', context)
