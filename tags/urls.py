from django.urls import path
from tags.views import Tag
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'',Tag)
urlpatterns = router.urls