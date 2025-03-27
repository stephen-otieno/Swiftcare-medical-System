"""
URL configuration for Medical project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path

from django.conf import settings
from django.views.static import serve

from swiftcare import views

urlpatterns = [

re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('patient_details/',views.patient_details,name='patient_details'),

    path('doctor_details/',views.doctor_details,name='doctor_details'),
    path('doctors/',views.view_doctors,name='doctors'),

    path('contact_us/',views.feedback, name='contact'),

    path('registered_patients/',views.registered_patients,name='registered_patients'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('medicine_details/', views.medicine, name='medicine_details'),

    path("appointment/<int:doctor_id>/", views.appointment, name="book_appointment"),

    path("scheduled_appointments/", views.scheduled_appointments, name="scheduled_appointments"),

    path('pay/', views.pay, name='pay'),

    path('payment-cancelled/', views.payment_failed, name='payment_cancelled'),

    path('payment-success/', views.payment_success, name='payment_success'),

    path('waiting/<int:transaction_id>/', views.waiting_page, name='waiting_page'),

    path('stk_push/', views.stk_push, name='stk_push'),

    path('callback', views.callback, name='callback'),

    path('check_status/<int:transaction_id>/', views.check_status, name='check_status'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
