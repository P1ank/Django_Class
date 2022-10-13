
from django.shortcuts import render
from django.http import HttpResponse
from.forms import InputForm
from.forms import GeeksForm
from django.forms import formset_factory
 
 
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
    context ={
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    # return response with template and context
    return render(request, "geeks.html", context)
