from django.urls import path, include
from rest_framework import routers
from .views import RecruiterViewSet, CandidateViewSet, JobViewSet, ApplyAPIView

router = routers.DefaultRouter()
router.register(r'recruiters', RecruiterViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('jobs/<int:job_id>/apply/', ApplyAPIView.as_view(), name='job-apply'),
]
