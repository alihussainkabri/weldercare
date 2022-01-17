from django.urls import path
from welderapp import views

urlpatterns = [
    path('', views.index),
    path('who-we-are/',views.whoWeAre),
    path('why-choose-us/',views.whyChooseUs),
    path('news/',views.news),
    path('contact/',views.contact),
    path('career/',views.career),
    path('tnc/',views.tnc),
    path('Privacy-Policy/',views.privacyPolicy),
    path('newsByMonth/<str:condition>',views.newsByMonth),
    path('contactPost/',views.contactPost),
    path('jobPost/',views.jobPost),
]