from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def show_popup(request):
    if request.method =="POST":
        new_percentage = request.POST['new_value']
        new_obj = models.Dropdown(value=new_percentage)
        new_obj.save()
        percentages = reversed(models.Dropdown.objects.all())
        print(percentages)
        return render(request,'home.html',{'percentages':percentages})
    percentages = models.Dropdown.objects.all()
    return render(request,'home.html',{'percentages':percentages})
