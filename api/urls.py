from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EducationViewSet, WorkExperienceViewSet, AwardViewSet, SkillViewSet,
    JobViewSet, CompanyViewSet, CatagoryViewSet, ApplicationViewSet, AccountViewSet
)

router = DefaultRouter()

router.register(r'jobs', JobViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'catagories', CatagoryViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'users', AccountViewSet, basename='users_details')
router.register(r'education', EducationViewSet)
router.register(r'work_experience', WorkExperienceViewSet)
router.register(r'award', AwardViewSet)
router.register(r'skill', SkillViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
