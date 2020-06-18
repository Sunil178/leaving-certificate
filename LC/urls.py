"""LC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lcapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('registrationform/', views.registrationform),
    path('registered/', views.registered),
    path('loginform/', views.loginform),
    path('loggedin/', views.loggedin),
    path('lc/', views.lc),
    path('genlc/', views.genlc),
    path('adddata/', views.adddata),
    path('enroll/', views.enroll),
    path('view_update/', views.showUpdate),
    path('update_page/', views.updatePage),
    path('update/', views.update),
    path('show_lc/', views.showLc),
    path('view_delete/', views.showDelete),
    path('delete/', views.delete),
    path('home/', views.home),
    path('logout/', views.logOut),
    path('form/', views.form),

]
