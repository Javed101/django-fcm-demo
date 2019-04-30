from django.urls import path
from web.views import index, serve_manifest, serve_firebase_messaging


urlpatterns = [
    path('', index, name="index-view"),
    path('manifest.json', serve_manifest),
    path('firebase-messaging-sw.js', serve_firebase_messaging),
]