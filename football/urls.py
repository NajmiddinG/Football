from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LigaViewSet, TeamViewSet, NewGameViewSet, OldGameViewSet

router = DefaultRouter()
router.register('liga', LigaViewSet, basename='liga')
router.register('team', TeamViewSet, basename='team')
router.register('newgame', NewGameViewSet, basename='newgame')
router.register('oldgame', OldGameViewSet, basename='oldgame')

urlpatterns = [
    path('', include(router.urls)),
]
