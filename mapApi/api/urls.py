from django.urls import path

from . import views

urlpatterns = [
    path('osm/<int:param1>/<int:param2>/<int:param3>', views.mapimage, name='mapimage'),
]