from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Landmark


class LandmarkList(ListView):
    model = Landmark
    template_name = 'landmarks.html'

class LandmarkDetail(DetailView):
    model = Landmark
    template_name = 'landmark_detail.html'