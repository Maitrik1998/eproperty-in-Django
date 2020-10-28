from . import views
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [

    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login_url/',LoginView.as_view(),name='login_url'),
	path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
	path('addproperty/',views.addproperty,name='addproperty'),
]