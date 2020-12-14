from django.urls import path
from newsletters.views import Newsletter
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'',Newsletter)
urlpatterns = router.urls