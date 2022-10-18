from django.contrib import admin
from django.urls import path
#now import the views.py file into this code
from . import views
from . import models
from .models import GeeksModel
from .views import geeks_view
from .views import GeeksList
from .views import GeeksDetailView
urlpatterns=[
  path('admin/',admin.site.urls),
  #path('',models.Humans), #was used for accesing django admin but couldnt proceed
  #path('',views.home_view), was used for initial forms
  #path('',views.formset_view),#used for Formset forms
  #path('', views.geeks_view),
  #path('', geeks_view), date time View
  #path('',GeeksModel),
  #path('',views.list_view),# first list view
  path('<id>', views.detail_view ),# detail view
  path('<id>/update/', views.update_view ),# update_view
  path('<id>/delete', views.delete_view ),#delete_view
  #path('',views.create_view),# function based create view
  #path('about/', MyView.as_view()),
  path('', GeeksList.as_view()),#retrieve View
  path('<pk>/', GeeksDetailView.as_view()),
]