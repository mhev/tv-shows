from django.urls import path
from . import views

urlpatterns = [
    path('', views.newshows),
    path('shows/new', views.newshows),
    path('addshow', views.addshow),
    path('displayshow/<show_id>', views.displayshow),
    path('deleteshow/<show_id>', views.deleteshow),
    path('editshow/<show_id>', views.editshow),
    path('process/<show_id>', views.process),
    path('display', views.display),
]