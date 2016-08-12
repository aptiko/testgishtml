from django.views.generic import CreateView

from .models import Polygon


class CreatePolygonView(CreateView):

    model = Polygon
    template_name = 'create_polygon.html'
    fields = ('mpoly',)
