from django.shortcuts import render,redirect

from app.forms import WardrobeForm
from app.models import Wardrobe

# Create your views here.
def index(request):
    if request.method == "POST":
        form = WardrobeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = WardrobeForm()
    return render(request, 'index.html',{"form":form})

def wardrobe_list(request):
    data=Wardrobe.objects.all()
    return render(request, 'list.html',{'data':data})