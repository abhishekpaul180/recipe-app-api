from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('/tags', views.TagViewSet)
router.register('/store_link', views.Store_linkViewSet)
app_name = 'picUploads'

urlpatterns = [
    path('', include(router.urls))
]
