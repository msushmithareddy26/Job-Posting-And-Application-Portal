from rest_framework import serializers
from .models import Recruiter, Candidate, Job, Application

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ['id','name','email']

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id','name','email','resume']

class ApplicationSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializer(read_only=True)
    candidate_id = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all(), source='candidate', write_only=True)

    class Meta:
        model = Application
        fields = ['id','candidate','candidate_id','job','applied_at']
        read_only_fields = ['id','applied_at','candidate']

class JobSerializer(serializers.ModelSerializer):
    recruiter = RecruiterSerializer(read_only=True)
    recruiter_id = serializers.PrimaryKeyRelatedField(queryset=Recruiter.objects.all(), source='recruiter', write_only=True)
    applicants_count = serializers.IntegerField(source='applications.count', read_only=True)

    class Meta:
        model = Job
        fields = ['id','title','description','required_skills','recruiter','recruiter_id','created_at','applicants_count']
        read_only_fields = ['id','created_at','applicants_count','recruiter']