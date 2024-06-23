"""
URL configuration for pizza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from . import views
# from homeapp import views as hv
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.login_view,name='login'),
    path('', include('orders.urls')),


    path('menu/',views.menu,name='menu'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('index/',views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('blog-single/',views.blog_single,name='blog-single'),
    # path('', include('orders.urls')),  # Include app-specific URLs
    path('login/',views.login_view,name='login'),
    # path('login/', views.login_view, name='login'),
    path('login/submit/', views.login_submit, name='login_submit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
