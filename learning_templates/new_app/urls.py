from django.conf.urls import url
from new_app import views

app_name = 'new_app'
urlpatterns = [
    url(r'^relative/$',views.relativepage,name = 'relative'),
    url(r'^home/$',views.homepage,name = 'home'),
    url(r'^about/$',views.aboutpage,name = 'about'),
]

