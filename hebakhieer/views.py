import json

import requests
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from khieerwebsite.settings import PROFILE_KEY, PAYTAB_API_SERVERKEY, API_ENDPOINT
from .models import HebaKheer, Volunteer


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
