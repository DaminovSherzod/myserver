from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    HTML = """
    <html>
    <head>
    <title>My App</title>
    </head>
    <body>
    <h1>My App</h1>
    <p>My App is Django app.</p>
    </body>
    </html>
    """
    return HttpResponse(HTML)