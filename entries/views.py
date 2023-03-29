from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.views.generic import ( ListView,DetailView,CreateView,UpdateView,DeleteView,)
from django.urls import reverse_lazy
from .models import Entry
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.


class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")
    template_name = 'entries/entry_list.html'

class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(SuccessMessageMixin,CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new entry was created!"

class EntryUpdateView(SuccessMessageMixin,UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.object.pk}
        )

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your entry was deleted!"


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)




def say_hello(request):
    return render(request,'entries/base.html')

def app(request):
    return render(request,'entries/app.html')

def logout(request):
    logout(request)
    return redirect('landing')


def login(request):
 if request.method == 'POST':
    username = request.POST.get('username') 
    pass1 = request.POST.get('pass1')  

    user = authenticate(request,username=username, password=pass1)
    if user is not None:
      
       
       return redirect ('app')

    else:
       messages.error(request, "Bad credentials")
       return redirect ('landing')  


 return render(request,'entries/login.html')

def signup(request):
    
    
 if request.method == "POST":
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']

    myuser = User.objects.create_user(username,email,pass1)
    myuser.first_name = firstname
    myuser.last_name = lastname
    myuser.save()
    messages.success (request, "Your account has been sucessfully created.")
    return redirect('list')
 
 return render(request,'entries/signup.html')


def list(request):
   return render(request, 'entries/entry_list.html')





def landing(request):
    return render(request,'entries/landing.html')






