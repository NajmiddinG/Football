from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewViewSet

router = DefaultRouter()
router.register('new', NewViewSet, basename='new')

urlpatterns = [
    path('', include(router.urls)),
]
