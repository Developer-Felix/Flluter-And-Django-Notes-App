from rest_framework import serializers
from .models import Note, Todo

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note 
        fields = ["id","title","body","created","updated"]

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id","name","priority","description","created"]