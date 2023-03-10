from django.db import models

class Job(models.Model):
    jobTitle = models.CharField(null=True, blank=True, max_length=1024)
    jobUrl = models.CharField(unique=True, null=True, blank=True, max_length=1024)
    companyName = models.CharField(null=True, blank=True, max_length=256)
    companyImageUrl = models.CharField(null=True, blank=True, max_length=2048)
    salary = models.IntegerField(null=True, blank=True,)
    isRemote = models.BooleanField(null=True, blank=True,)
    jobType = models.CharField(null=True, blank=True, max_length=32)
    experience = models.CharField(null=True, blank=True, max_length=32)
    website = models.CharField(null=True, blank=True, max_length=64)
    websiteIcon = models.CharField(null=True, blank=True, max_length=2048)
    creationTime = models.DateTimeField(auto_now_add=True, null=True, blank=True,)

    unique_together = [['jobTitle', 'jobUrl']]


    def __str__(self) -> str:
        return f'{self.jobTitle}'

