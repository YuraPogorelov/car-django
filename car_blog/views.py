from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from .models import Characteristics


class CharacteristicsView(View):

    def get(self, request):
        characteristics = Characteristics.objects.all()
        return render(request, "characteristics/characteristics_list.html", {"characteristics_list": characteristics})
