from django.db import models
from django.conf import settings
from jobs.models import Job


class Application(models.Model):
    STATUS_CHOICES = (
        ("applied", "Applied"),
        ("shortlisted", "Shortlisted"),
        ("interview", "Interview"),
        ("selected", "Selected"),
        ("rejected", "Rejected"),
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    candidate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applicatoins",
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="applied")
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("job", "candidate")

    def __str__(self):
        return f"{self.candidate.email}-> {self.job.title}"
