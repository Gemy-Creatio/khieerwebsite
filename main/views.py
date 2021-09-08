from django.shortcuts import render, redirect

from main.models import Contact, TechnicalSupport


def home_page(request):
    return render(request, 'main/home.html', )


def about_page(request):
    return render(request, 'main/about.html')


def ethics_page(request):
    return render(request, 'main/ethics.html')


def roaya_page(request):
    return render(request, 'main/roaya.html')


def khieer30_page(request):
    return render(request, 'main/khieer2030.html')


def staff_page(request):
    return render(request, 'main/who-us.html')


def paramg_page(request):
    return render(request, 'main/paramg.html')


def autoservices(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(
            name=name, address=address, phone=phone, message=message)
        contact.save()
        if contact.pk:
            redirect('home-page')
        else:
            redirect('auto-page')
    return render(request, 'main/autoservice.html')


def tech_support(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        tech_support = TechnicalSupport(name=name, message=message)
        tech_support.save()
        if tech_support.pk:
            redirect('home-page')
        else:
            redirect('tech-page')
    return render(request, 'main/tech-support.html')
