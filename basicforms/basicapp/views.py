from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contact
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')



def form_name_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou') 

    return render(request, 'basicapp/form_basic.html', {'form': form})

def thank_you_view(request):
    submissions = Contact.objects.all()
    return render(request, 'basicapp/thankyou.html', {'submissions': submissions})