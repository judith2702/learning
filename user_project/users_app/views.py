from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from users_app.models import User
# Create your views here.
def index(request):
    return render(request, 'users_app/index.html')


def user(request):
    users_list = User.objects.all()
    user_data = {'users_list': users_list}
    return render(request, 'users_app/users.html', context=user_data)