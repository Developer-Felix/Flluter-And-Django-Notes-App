from rest_framework.decorators import api_view
from rest_framework.response import Response

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
