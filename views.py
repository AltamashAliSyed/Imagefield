from django.shortcuts import render,redirect,get_object_or_404
from .models import Image
from .forms import ImageForm
# Create your views here.
def showimage(request):
  image = Image.objects.all()
  return render(request,'showimage.html',{'image':image})

def postimage(request):
  if request.method == "POST":
    fm = ImageForm( request.POST,request.FILES)
    if fm.is_valid():
      fm.save()
      return redirect('showimage')
  else:
    fm = ImageForm()
    
  return render(request,'postimage.html',{'form':fm})

