from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from .views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]