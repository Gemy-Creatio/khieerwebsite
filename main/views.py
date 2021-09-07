from django.shortcuts import render


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
