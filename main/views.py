from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import View
from accounts.models import User
from main.models import Contact, TechnicalSupport , TopicGreen
from greenCircle.models import Course, Trainer
from hebakhieer.models import HebaKheer, Volunteer
from main.forms import (
    TopicForm
)
from django.views.generic import CreateView , View
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
import json
import requests
from khieerwebsite.settings import PROFILE_KEY, PAYTAB_API_SERVERKEY, API_ENDPOINT

class AllTopicDash(View):
    def get(self , request):
        topics = TopicGreen.objects.all()
        paginator = Paginator(topics, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {"topics": page_obj}
        return render(request , 'main/alltopics.html' , context=context)




class CreateTopic(CreateView):
    model = TopicGreen
    form_class = TopicForm
    template_name = 'main/add-topic.html'
    def form_valid(self, form):
        if self.request.POST.get('is_paid') == 'True':
            topic = form.save(commit=True)
            topic.save()
            payload = {
            "profile_id": PROFILE_KEY,
            "tran_type": "sale",
            "tran_class": "ecom",
            "cart_description": "دفع رسوم رفع القضية",
            "cart_id": "50",
            "cart_currency": "sar",
            "cart_amount": int(250),
            "callback": f"{reverse('home-page')}",
            "return":  f"{reverse('home-page')}"
            }
            headers = {
            "authorization": PAYTAB_API_SERVERKEY,
            "Content-Type": 'application/json; charset=utf-8'
           }
            r = requests.post(API_ENDPOINT, data=json.dumps(payload), headers=headers)
            data = json.dumps(r.json())
            content = json.loads(data)
            return redirect(content['redirect_url'])
        else:
             messages.info(self.request, "يجب دفع الرسوم لتتمكن من رفع قضيتك        ")
             return reverse('add-topic')

    def get_success_url(self):
        messages.success(self.request, "شكرا لرفع قضيتك        ")
        return reverse('add-topic')


def page_not_found(request , exception):
    return render(request, 'main/error404.html')


def Error500(request):
    return render(request, 'main/error404.html')


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
    durations = HebaKheer.objects.order_by('-ammount')[:5]
    for heba in hebs:
        hebalabels.append(heba.name)
        hebadata.append(heba.ammount)
    for dur in durations:
        durationlabels.append(dur.name)
        durationdata.append(dur.ammount)
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


# class VolunteerAllReport(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('volunteer-all-pdf.html')
#         needyinshow = Volunteer.objects.all()
#         user_obj = User.objects.get(pk=request.user.pk)
#         context = {
#             "company": "خير السعوديه",
#             "user": user_obj,
#             "vols": needyinshow,
#             "topic": "المتقدمين للتطوع ",
#             "today": datetime.today().strftime('%Y-%m-%d'),
#         }
#         html = template.render(context)
#         pdf = render_to_pdf('volunteer-all-pdf.html', context)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Invoice_%s.pdf" % ("12341231")
#             content = "inline; filename='%s'" % (filename)
#             download = request.GET.get("download")
#             if download:
#                 content = "attachment; filename='%s'" % (filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not found")


def reports(request):
    return render(request, 'main/reports.html')


# class HebaAllReport(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('heba-all-pdf.html')
#         needyinshow = HebaKheer.objects.all()
#         user_obj = User.objects.get(pk=request.user.pk)
#         context = {
#             "company": "خير السعوديه",
#             "user": user_obj,
#             "hebas": needyinshow,
#             "topic": "هبات الخير ",
#             "today": datetime.today().strftime('%Y-%m-%d'),
#         }
#         html = template.render(context)
#         pdf = render_to_pdf('heba-all-pdf.html', context)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Invoice_%s.pdf" % ("12341231")
#             content = "inline; filename='%s'" % (filename)
#             download = request.GET.get("download")
#             if download:
#                 content = "attachment; filename='%s'" % (filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not found")


# class CourseAllReport(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('course-all-pdf.html')
#         needyinshow = Course.objects.all()
#         user_obj = User.objects.get(pk=request.user.pk)
#         context = {
#             "company": "خير السعوديه",
#             "user": user_obj,
#             "courses": needyinshow,
#             "topic": "الحقائب الخضراء ",
#             "today": datetime.today().strftime('%Y-%m-%d'),
#         }
#         html = template.render(context)
#         pdf = render_to_pdf('course-all-pdf.html', context)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Invoice_%s.pdf" % ("12341231")
#             content = "inline; filename='%s'" % (filename)
#             download = request.GET.get("download")
#             if download:
#                 content = "attachment; filename='%s'" % (filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not found")
