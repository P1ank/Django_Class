
from django.shortcuts import  (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http import HttpResponse
from.forms import InputForm
from.forms import GeeksForm
from .models import GeeksModel
from django.forms import formset_factory
import datetime
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
 
def index(request):# for printing hello geeks in the view page
  return HttpResponse("Hello Geeks")

def home_view(request):# for displaying forms for clients
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)

def formset_view(request):# for Django Formset
    context ={}
  
    # creating a formset
    GeeksFormSet = formset_factory(GeeksForm) #extra= 5 used to make 5 form inquiries
    formset = GeeksFormSet()#(request.POST or None) used to display inputs at the terminal
    
    #if formset.is_valid():
        #for form in formset:
            #print(form.cleaned_data)
              
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "home.html", context)

def geeks_view(request):
    # create a dictionary to pass
    # data to the template
    """context ={
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    # return response with template and context
    return render(request, "geeks.html", context)"""
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
         
    return render(request, "list_view.html", context)

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)

def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id = id)
         
    return render(request, "detail_view.html", context)

def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)

def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')

class GeeksList(ListView):
 
    # specify the model for list view
    model = GeeksModel

class GeeksDetailView(DetailView):
    # specify the model to use
    model = GeeksModel
