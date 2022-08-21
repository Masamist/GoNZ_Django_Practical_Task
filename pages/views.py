from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import Tour
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

User = get_user_model()


# Modify tours info

# Create your views here.


class IndexView(TemplateView):
    template_name = "pages/index.html"


# Tours
class TourView(ListView):
    model = Tour
    template_name = "pages/tour.html"


class TourDetailView(DetailView):
    model = Tour
    template_name = "pages/tour_detail.html"


class TourCreateView(CreateView):
    model = Tour
    template_name = "pages/tour_create.html"

    fields = ["tour_name", "agent", "city_name",
              "date", "duration", "price", "body"]


class TourUpdateView(UpdateView):
    model = Tour
    template_name = "pages/tour_update.html"

    fields = ["tour_name", "city_name", "date", "duration", "price", "body"]


class TourDeleteView(DeleteView):
    model = Tour
    template_name = "pages/tour_delete.html"
    success_url = reverse_lazy("tour")

# Agents


class AgentView(ListView):
    model = User
    template_name = "pages/agent.html"


class AgentDetailView(DetailView):
    model = User
    template_name = "pages/agent_detail.html"
