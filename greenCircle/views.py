from django.shortcuts import render, redirect
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
