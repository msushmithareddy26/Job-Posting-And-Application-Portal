from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Recruiter, Job  # adjust import path if needed

class JobTests(TestCase):
    def setUp(self):
        """
        Set up the test environment before each test runs:
        - Create a test user
        - Create a recruiter
        - Authenticate the API client
        - Prepare sample job data
        """
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        # Create a recruiter (adjust fields to match your model)
        self.recruiter = Recruiter.objects.create(
            name="Test Recruiter",
            email="recruiter@test.com"
        )

        # Initialize API client and authenticate
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Job data (only fields that exist in your model)
        self.job_data = {
            "title": "Software Engineer",
            "description": "Develop backend APIs",
            "required_skills": "",
            "recruiter_id": self.recruiter.id
        }

    def test_create_job(self):
        """
        Test creating a new job via POST request.
        Expected outcome: HTTP 201 Created
        """
        response = self.client.post("/api/jobs/", self.job_data, format='json')
        print(response.data)  # Optional debug output
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_jobs(self):
        """
        Test retrieving all jobs via GET request.
        Steps:
        1. Create a job
        2. Retrieve jobs
        Expected outcome: at least one job exists
        """
        self.client.post("/api/jobs/", self.job_data, format='json')
        response = self.client.get("/api/jobs/")
        print(response.data)  # Optional debug output
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_update_job(self):
        """
        Test updating an existing job via PUT request.
        Steps:
        1. Create a job
        2. Update job fields
        Expected outcome: HTTP 200 OK and database reflects changes
        """
        # Create a job first
        create_response = self.client.post("/api/jobs/", self.job_data, format='json')
        job_id = create_response.data['id']

        # Updated data (only existing fields)
        updated_data = {
            "title": "Senior Software Engineer",
            "description": "Develop and design backend APIs",
            "required_skills": "Python, Django",
            "recruiter_id": self.recruiter.id
        }

        # Send PUT request
        update_response = self.client.put(f"/api/jobs/{job_id}/", updated_data, format='json')
        print(update_response.data)  # Optional debug output
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)

        # Check database values directly
        job_instance = Job.objects.get(id=job_id)
        self.assertEqual(job_instance.title, "Senior Software Engineer")
        self.assertEqual(job_instance.description, "Develop and design backend APIs")
        self.assertEqual(job_instance.required_skills, "Python, Django")

    def test_delete_job(self):
        """
        Test deleting a job via DELETE request.
        Steps:
        1. Create a job
        2. Delete the job
        3. Attempt to retrieve deleted job
        Expected outcome: HTTP 204 No Content on delete, 404 Not Found afterward
        """
        # Create a job first
        create_response = self.client.post("/api/jobs/", self.job_data, format='json')
        job_id = create_response.data['id']

        # Delete the job
        delete_response = self.client.delete(f"/api/jobs/{job_id}/")
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify the job no longer exists
        get_response = self.client.get(f"/api/jobs/{job_id}/")
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)
