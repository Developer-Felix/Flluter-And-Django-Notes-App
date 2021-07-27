import uuid
from django.db import models

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255,default="None")
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['-updated']


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    Prio = ((1,"A"),(2,"B"),(3,"B"),)
    priority = models.IntegerField(choices=Prio,default=1)
    description = models.TextField()
    duedate = models.DateTimeField(auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name[0:50]

    class Meta:
        ordering = ['-created']