from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions, generics, status
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
    return Response({"success": True, 
                             "errors": None, 
                             "status_code": 0,
                             "status_message": "successfully reatrived all users",
                             "message": "successfully reatrived all users",
                             "data": serializer.data}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def getNote(request,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note,many=False)
    return Response({"success": True, 
                             "errors": None, 
                             "status_code": 0,
                             "status_message": "successfully reatrived a note",
                             "message": "successfully reatrived a note",
                             "data": serializer.data}, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def createNote(request):
    data = request.data 
    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note,many=False)
    return Response({"success": True, 
                             "errors": None, 
                             "status_code": 0,
                             "status_message": "successfully saved notes details",
                             "message": "successfully saved the notes","data": serializer.data}, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
def updateNote(request,pk):
    data = request.data 
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"success": True, 
                             "errors": None, 
                             "status_code": 0,
                             "status_message": "successfully updated notes details",
                             "message": "successfully updated the notes","data": serializer.data}, status=status.HTTP_201_CREATED)

@api_view(["DELETE"])
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response({"success": True, 
                             "errors": None, 
                             "status_code": 0,
                             "status_message": "successfully deleted",
                             "message": "successfully deleted"}, status=status.HTTP_201_CREATED)




@api_view(["GET"])
def getTodos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos,many=True)
    return Response({"success": True, 
                             "errors": None, 
                             "status_code": 0,
                             "status_message": "successfully reatrived all notes",
                             "message": "successfully reatrived all users",
                             "data": serializer.data}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def getTodo(request,pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo,many=False)
    return Response({"success": True, 
                             "errors": None, 
                             "status_code": 0,
                             "status_message": "successfully reatrived a todo",
                             "message": "successfully reatrived a todo",
                             "data": serializer.data}, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def createTodo(request):
    data = request.data 
    todo = Todo.objects.create(
        body = data['body']
    )
    serializer = TodoSerializer(todo,many=False)
    return Response({"success": True, 
                             "errors": None, 
                             "status_code": 0,
                             "status_message": "successfully save todos details",
                             "message": "successfully saved the todoss","data": serializer.data}, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
def updateTodo(request,pk):
    data = request.data 
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"success": True, 
                             "errors": None, 
                             "status_code": 0,
                             "status_message": "successfully updated todos details",
                             "message": "successfully updatedd the todoss","data": serializer.data}, status=status.HTTP_201_CREATED)

@api_view(["DELETE"])
def deleteTodo(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response({"success": True, 
                             "errors": None, 
                             "status_code": 0,
                             "status_message": "successfully deleted",
                             "message": "successfully deleted"}, status=status.HTTP_201_CREATED)