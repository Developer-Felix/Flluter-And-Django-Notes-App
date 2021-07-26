from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
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