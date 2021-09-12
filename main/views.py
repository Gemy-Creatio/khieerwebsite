from django.shortcuts import render, redirect

from main.models import Contact, TechnicalSupport
from greenCircle.models import Course, Trainer
from hebakhieer.models import HebaKheer


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


def media_center(request):
    return render(request, 'main/mediaCenter.html')


def dashboard(request):
    labels = []
    data = []
    trainerlabels = []
    trainerdata = []
    hebalabels = []
    hebadata = []
    durationlabels = []
    durationdata = []
    hebs = HebaKheer.objects.order_by('-ammount')[:5]
    durations = Course.objects.order_by('-duration')[:5]
    for heba in hebs:
        hebalabels.append(heba.name)
        hebadata.append(heba.ammount)
    for dur in durations:
        durationlabels.append(dur.name)
        durationdata.append(dur.duration)
    trainers = Trainer.objects.order_by('-courses')[:5]
    for trainer in trainers:
        trainerlabels.append(trainer.first_name)
        trainerdata.append(trainer.courses.count())
    queryset = Course.objects.order_by('-Requests')[:5]
    for course in queryset:
        labels.append(course.name)
        data.append(course.Requests.count())
    context = {
        'labels': labels,
        'data': data,
        'trainerslabels': trainerlabels,
        'trainersdata': trainerdata,
        'hebaslabales': hebalabels,
        'hebadata': hebadata,
        'durlabels': durationlabels,
        'durdata': durationdata,
    }
    return render(request, 'main/dashboard.html', context=context)
