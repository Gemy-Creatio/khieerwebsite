from django.shortcuts import render , redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView
from . import models , forms
from django.core.files.storage import FileSystemStorage

# Create your views here.
def addUserDesign(request):
    if request.method == 'POST' and request:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        name = request.POST.get('name')
        obj = models.KhieerDesign(name=name , image = image)
        obj.save()
        if obj.pk:
            return redirect('user-designs')
    return render(request, 'designkhieer/addUserDesign.html')


def AddDesign(request):
    if request.method == 'POST' and request:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        name = request.POST.get('name')
        obj = models.KhieerDesign(name=name , image = image)
        obj.save()
        if obj.pk:
            return redirect('all-design')
    return render(request, 'designkhieer/addDesign.html')    


class AllDesigns(View):
    def get(self, request):
        data = models.KhieerDesign.objects.all()
        return render(request, 'designkhieer/allDesigns.html', context={"data": data})            





class AllUserDesigns(View):
    def get(self, request):
        data = models.KhieerDesign.objects.all()
        return render(request, 'designkhieer/userDesigns.html', context={"data": data})                    