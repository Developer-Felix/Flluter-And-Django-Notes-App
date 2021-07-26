from django.http import JsonResponse

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
    return JsonResponse(routes,safe=False)
