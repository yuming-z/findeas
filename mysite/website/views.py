from django.shortcuts import render
from django.http import HttpResponse

def validate(request):
    '''This function is used to validate the connection to the database.'''

    success = "The connection for data fetching is successful."

    return HttpResponse(status=200, content=success)