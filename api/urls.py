from django.urls import path
from .views import getRoutes,getNotes,getNote

urlpatterns = [
    path('',getRoutes),
    path('notes/',getNotes),
    path('notes/<str:pk>/',getNote),
]
