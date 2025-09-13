from django.db import models

class Recruiter(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def _str_(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    resume = models.TextField(blank=True)  # or a FileField for real files

    def _str_(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.TextField(blank=True)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name='jobs')
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

class Application(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('candidate', 'job')

    def _str_(self):
        return f"{self.candidate} -> {self.job}"

