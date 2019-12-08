"""fb URL Configuration

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
from fbapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginPage),
    path('register/<str:image>', views.register),
    path('view_register/', views.viewRegister),
    path('check_login/', views.checkLogin),
    path('index/', views.index),
    path('edit_profile/<int:id>', views.editProfile),
    path('profile_updated/<int:id>', views.profileUpdated),
    path('send_request/<int:id>', views.sendRequest),
    path('show_request/', views.showRequest),
    path('my_profile/', views.myProfile),
    path('pending_requests/', views.pendingRequests),
    path('accept_request/<int:id>', views.acceptRequest),
    path('requested_friends/', views.requestedFriends),
]
