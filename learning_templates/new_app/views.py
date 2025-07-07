from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'new_app/base.html')

def homepage(request):
    return render(request,'new_app/home.html')

def aboutpage(request):
    return render(request,'new_app/about.html')

def relativepage(request):
    return render(request,'new_app/relative_url_template.html')

