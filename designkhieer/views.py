from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import get_language
from django.views import View
from django.views.generic.edit import CreateView
from . import models, forms
from django.core.files.storage import FileSystemStorage
from .models import (
    DesignRequest
)


class NewUserDesign(View):
    def get(self, request):
        data = models.KhieerDesign.objects.order_by('-pk')
        paginator = Paginator(data, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'designkhieer/newUserDesign.html', context={"data": page_obj})


# Create your views here.
def addUserDesign(request):
    if request.method == 'POST' and request:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        name = request.POST.get('name')
        obj = models.KhieerDesign(name=name, image=image)
        obj.save()
        if obj.pk:
            return redirect('new-designs')
    return render(request, 'designkhieer/addUserDesign.html')


# def AddDesign(request):
#     if request.method == 'POST' and request:
#         image = request.FILES['image']
#         fs = FileSystemStorage()
#         filename = fs.save(image.name, image)
#         name = request.POST.get('name')
#         obj = models.KhieerDesign(name=name, image=image)
#         obj.save()
#         if obj.pk:
#             return redirect('all-design')
#     return render(request, 'designkhieer/addDesign.html')

class AddDesign(CreateView):
    model = models.KhieerDesign
    template_name = 'designkhieer/addUserDesign.html'
    form_class = forms.KhieerDesignForm

    def get_success_url(self):
        return reverse('new-designs')


class AllDesigns(View):
    def get(self, request):
        data = models.KhieerDesign.objects.all()
        paginator = Paginator(data, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'designkhieer/allDesigns.html', context={"data": page_obj})


def AddUserRequestDesign(request):
    if request.method == 'POST' and request.is_ajax:
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        number = request.POST.get('number')
        type = request.POST.get('type')
        color = request.POST.get('color')
        design = request.POST.get('design')
        req = DesignRequest(product='تى شيرت', design_image_id=design, email=email, phone=phone, name=name,
                            number_of_order=number,
                            type_clothes=type, color=color)
        req.save()
        code = get_language()
        if req is not None:
            if code == 'ar':
                messages.success(request, "نشكر لكم طلبكم من متجرنا و تسرنا خدمتكم")
                return JsonResponse({"status": 1})
            else:
                messages.success(request, "We thank you for your order from our store and we are pleased to serve you")
                return JsonResponse({"status": -1})
        else:
            if code == 'ar':
                messages.error(request, "حدث خطأ حاول مرة أخرى")
                return JsonResponse({"status": 1})
            else:
                messages.error(request, "Error Happened Try For another Time")
                return JsonResponse({"status": -1})


class AllUserDesigns(View):
    def get(self, request):
        data = models.KhieerDesign.objects.order_by('-pk')
        paginator = Paginator(data, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'designkhieer/userDesigns.html', context={"data": page_obj})


def DeleteDesign(request, pk):
    models.KhieerDesign.objects.filter(id=pk).delete()
    return redirect('new-designs')
