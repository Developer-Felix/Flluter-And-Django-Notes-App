from django.urls import path
from .views import createTodo, deleteTodo, getRoutes,getNotes,getNote,createNote, getTodo, getTodos,updateNote,deleteNote, updateTodo

urlpatterns = [
    path('',getRoutes),
    path('todos/',getTodos),
    path('todos/create/',createTodo),
    path('todos/<str:pk>/',getTodo),
    path('todos/<str:pk>/update/',updateTodo),
    path('todos/<str:pk>/delete/',deleteTodo),

    path('notes/',getNotes),
    path('notes/create/',createNote),
    path('notes/<str:pk>/',getNote),
    path('notes/<str:pk>/update/',updateNote),
    path('notes/<str:pk>/delete/',deleteNote),
]
