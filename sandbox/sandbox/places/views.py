from django.views import generic
from . import models


class PlaceListView(generic.ListView):
    model = models.Place