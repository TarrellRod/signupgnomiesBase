from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from users.forms import CategoryForm, SlotForm

events = [{
    'name':'class lunch',
    'teacher':'sytsma',
    'date':'09-24-2023'
},
{
    'name':'class trip',
    'teacher':'sytsma',
    'date':'09-25-2023'
}
]

# Create your views here.
def home(request):
    events = models.Event.objects.all()
    context = {
        'events':events
    }
    return render(request, "signupgnomies/home.html", context)
    #return HttpResponse("<h1>Signup app</h1>")

class EventsListView(ListView):
    model= models.Event
    template_name= 'signupgnomies/home.html'
    context_object_name='events'

class EventDetailView(DetailView):
    model = models.Event

class EventCreateView(LoginRequiredMixin,CreateView):
    model = models.Event
    fields = ['event_name', 'description','date']

class EventUpdateView(LoginRequiredMixin,CreateView,UpdateView):
    model = models.Event
    fields = ['event_name', 'description','date']

class EventDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Event
    success_url = reverse_lazy('home')

class CategoryDetailView(DetailView):
    model = models.Category

class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = models.Category
    form_class = CategoryForm
    #fields = ['name']

    def form_valid(self, form):
        form.instance.event_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class SlotCreateView(LoginRequiredMixin,CreateView):
    model = models.Slot
    form_class = SlotForm
    #fields = ['name']

    def form_valid(self, form):
        form.instance.category_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

def about(request):
    return render(request, "signupgnomies/about.html")
    #return HttpResponse("<h1>this is about<h1>")