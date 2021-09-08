from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from greenCircle.models import Trainer
from hebakhieer.models import Volunteer
from .models import User
from django.core.files.storage import FileSystemStorage


def register_trainer(request):
    if request.method == 'POST' and request:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        train = Trainer(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address,
                        image=image)
        train.save()
        if train.pk:
            return redirect('home-page')
    return render(request, 'accounts/register-trainer.html')


def loginPage(request):
    if request.method == 'POST' and request.is_ajax:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('user-profile-dash')
        else:
            return JsonResponse({"status": 'Username OR password is incorrect'})
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def register_secondary_empolyee(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_secondary_empuser(email=email, first_name=first_name, last_name=last_name,
                                                     address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('home-page')
    context = {}
    return render(request, 'accounts/register-employee.html', context)


def register_helper_employee(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_helper_empuser(email=email, first_name=first_name, last_name=last_name,
                                                  address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('home-page')
    context = {}
    return render(request, 'accounts/register-helper-employee.html', context)


def register_volunteer(request):
    if request.method == 'POST' and request.FILES['cv']:
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        filed = request.POST.get('filed')
        study = request.POST.get('study')
        goals = request.POST.get('goals')
        bithdate = request.POST.get('bithdate')
        skills = request.POST.get('skills')
        time = request.POST.get('time')
        place = request.POST.get('place')
        cv = request.FILES['cv']
        gender = request.POST.get('gender')
        fs = FileSystemStorage()
        fs.save(cv.name, cv)
        job = request.POST.get('job')
        desc = request.POST.get('specific')
        vol_profile = Volunteer(job=job, phone=phone, address=address, desc=desc, first_name=first_name, email=email,
                                gender=gender, birthdate=bithdate,
                                time=time, place=place, cv=cv, skills=skills, study=study, goals=goals,
                                filed=filed, last_name=last_name)
        vol_profile.save()
        if vol_profile is not None:
            return redirect('home-page')
        else:
            redirect('reg-vol')
    context = {}
    return render(request, 'accounts/register-volunteer.html', context)


def user_profile(request):
    return render(request, 'accounts/user-profile.html')


def user_profile_dash(request):
    return render(request, 'accounts/profile-dash.html')


def edit_user_info(request, pk):
    user_obj = User.objects.get(pk=pk)
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_obj.email = email
        user_obj.address = address
        user_obj.first_name = first_name
        user_obj.phone = phone
        user_obj.last_name = last_name
        user_obj.save()
        return redirect('user-profile')
    return render(request, 'accounts/user_edit.html', context={"user": user_obj})


def employees_list(request):
    context = {"employees": User.objects.exclude(user_type=1)}
    return render(request, 'accounts/employees_list.html', context=context)
