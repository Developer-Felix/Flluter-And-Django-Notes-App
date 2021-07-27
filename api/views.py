from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer,TodoSerializer
from .models import Note,Todo
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
        'Endpoint':'/notes/',
        'method':'GET',
        'body':None,
        'description':'Hae Ninga'
        },
        {
        'Endpoint':'/notes/id',
        'method':'GET',
        'body':None,
        'description':'Hae Ninga'
        },
        {
        'Endpoint':'/notes/create',
        'method':'POST',
        'body':None,
        'description':'Hae Ninga'
        },
        {
        'Endpoint':'/notes/id/update',
        'method':'PUT',
        'body':None,
        'description':'Hae Ninga'
        },
        {
        'Endpoint':'/notes/id/delete',
        'method':'DELETE',
        'body':None,
        'description':'Hae Ninga'
        },
    ]
    return Response(routes)

@api_view(["GET"])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getNote(request,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(["POST"])
def createNote(request):
    data = request.data 
    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def updateNote(request,pk):
    data = request.data 
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note is deleted')




@api_view(["GET"])
def getTodos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos,many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getTodo(request,pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo,many=False)
    return Response(serializer.data)

@api_view(["POST"])
def createTodo(request):
    data = request.data 
    todo = Todo.objects.create(
        body = data['body']
    )
    serializer = TodoSerializer(todo,many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def updateTodo(request,pk):
    data = request.data 
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteTodo(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response('Todo is deleted')