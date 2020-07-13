from django.urls import path

from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('drop', views.add_file, name='drop'),
    # path(notes,views.add_notes,name='notes')
]
