import json

import requests
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from accounts.models import User
from khieerwebsite.settings import PROFILE_KEY, PAYTAB_API_SERVERKEY, API_ENDPOINT
from .models import HebaKheer, Volunteer
from django.core.paginator import Paginator


# Create your views here.
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
        bithdate = request.POST.get('birthdate')
        skills = request.POST.get('skills')
        time = request.POST.get('time')
        place = request.POST.get('place')
        cv = request.FILES['cv']
        gender = request.POST.get('gender')
        fs = FileSystemStorage()
        fs.save(cv.name, cv)
        job = request.POST.get('job')
        desc = request.POST.get('specific')
        try:
            vol_profile = Volunteer.objects.create(job=job, phone=phone, address=address, desc=desc,
                                                   first_name=first_name, email=email,
                                                   gender=gender, birthdate=bithdate,
                                                   time=time, place=place, cv=cv, skills=skills, study=study,
                                                   goals=goals,
                                                   filed=filed, last_name=last_name)
            return redirect('home-page')

        except:
            redirect('reg-vol')
    context = {}
    return render(request, 'hebakhieer/volunteer-user.html', context)


def heba_khieer(request):
    if request.method == 'GET':
        return render(request, 'hebakhieer/hebakhieer.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        ammount = request.POST.get('amount')
        heba_obj = HebaKheer(
            address=address, phone=phone, name=name, ammount=ammount)
        payload = {
            "profile_id": PROFILE_KEY,
            "tran_type": "sale",
            "tran_class": "ecom",
            "cart_description": "هبة مساعدة لجمعية خير السعودية",
            "cart_id": "50",
            "cart_currency": "sar",
            "cart_amount": int(ammount),
            "callback": "https://khieer.com/about",
            "return": "https://khieer.com/"
        }
        headers = {
            "authorization": PAYTAB_API_SERVERKEY,
            "Content-Type": 'application/json; charset=utf-8'
        }
        r = requests.post(API_ENDPOINT, data=json.dumps(payload), headers=headers)
        data = json.dumps(r.json())
        content = json.loads(data)
        heba_obj.save()
        return redirect(content['redirect_url'])


def dash_options(request):
    return render(request, 'hebakhieer/dash-options.html')


def dash_emps(request):
    emps = User.objects.exclude(user_type=1)
    paginator = Paginator(emps, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "emps": page_obj
    }
    return render(request, 'hebakhieer/dash-emps.html', context=context)


def dash_heba(request):
    hebas = HebaKheer.objects.all()
    paginator = Paginator(hebas, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "hebas": page_obj
    }
    return render(request, 'hebakhieer/heba-dash.html', context=context)


def dash_volunteer(request):
    vols = Volunteer.objects.all()
    paginator = Paginator(vols, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "vols": page_obj
    }
    return render(request, 'greenCircle/all-volunteers.html', context=context)


def vol_details(request, pk):
    vol = Volunteer.objects.get(pk=pk)
    context = {
        "vol": vol
    }
    return render(request, 'hebakhieer/detail-volunteer.html', context=context)
