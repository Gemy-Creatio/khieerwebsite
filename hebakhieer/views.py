import json

import requests
from django.shortcuts import render, redirect

from khieerwebsite.settings import PROFILE_KEY, PAYTAB_API_SERVERKEY, API_ENDPOINT
from .models import HebaKheer


# Create your views here.


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
