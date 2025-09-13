from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Recruiter, Candidate, Job, Application
from .serializers import RecruiterSerializer, CandidateSerializer, JobSerializer, ApplicationSerializer
from rest_framework.views import APIView

class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer

    @action(detail=True, methods=['get'])
    def applicants(self, request, pk=None):
        # relational query: return candidates for given job
        job = get_object_or_404(Job, pk=pk)
        apps = Application.objects.filter(job=job).select_related('candidate')
        candidates = [app.candidate for app in apps]
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

class ApplyAPIView(APIView):
    def post(self, request, job_id):
        job = get_object_or_404(Job, pk=job_id)
        candidate_id = request.data.get('candidate_id')
        if not candidate_id:
            return Response({'detail': 'candidate_id required'}, status=status.HTTP_400_BAD_REQUEST)
        candidate = get_object_or_404(Candidate, pk=candidate_id)
        # Create application if not exists
        application, created = Application.objects.get_or_create(candidate=candidate, job=job)
        serializer = ApplicationSerializer(application)
        if created:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'Already applied'}, status=status.HTTP_200_OK)
