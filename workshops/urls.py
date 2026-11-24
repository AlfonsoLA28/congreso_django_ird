from django.urls import path

from . import views

app_name = "workshops"
urlpatterns = [
    path('', views.workshop_list, name="list"), # workshop:list
    path('<int:id>/', views.workshops_details, name="details")
]