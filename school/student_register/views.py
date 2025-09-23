from django.shortcuts import render,HttpResponse,render
from .forms import RegistrationForm


# Create your views here.
def index(request):
    if request.method == 'POST' :
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successful")
    else :
        form = RegistrationForm()

    return render(request,'registrationForm.html',{'form':form})