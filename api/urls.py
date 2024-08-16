from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'task', views.TasksViewSet)
router.register(r'comment', views.CommentsViewSet)

urlpatterns = [
    path('', include(router.urls))
]