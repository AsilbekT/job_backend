from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, CompanyViewSet, CatagoryViewSet, ApplicationViewSet

router = DefaultRouter()

router.register(r'jobs', JobViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'catagories', CatagoryViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
