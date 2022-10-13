from django.contrib import admin
from django.urls import path
#now import the views.py file into this code
from . import views
from . import models
urlpatterns=[

  #path('',models.GeeksModel), was used for accesing django admin but couldnt proceed
  #path('',views.home_view), was used for initial forms
  #path('',views.formset_view),#used for Formset forms
  path('', views.geeks_view),
]