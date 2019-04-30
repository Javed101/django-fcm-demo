from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def serve_manifest(request):
    f = open('web/static/manifest.json').read()
    return HttpResponse(f, content_type='application/javascript')


def serve_firebase_messaging(request):
    f= open('web/static/js/firebase-messaging-sw.js').read()
    return HttpResponse(f,content_type="application/javascript")


def index(request, **kwargs):
    """
    home page view
    """
    context = {}
    return render(request, "index.html", context)
