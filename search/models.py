from django.db import models

class Job(models.Model):
    jobTitle = models.CharField(null=True, max_length=1024)
    jobUrl = models.CharField(null=True, max_length=1024)
    companyName = models.CharField(null=True, max_length=256)
    companyImage = models.ImageField(null=True, upload_to='company/logo-social.png')
    salary = models.IntegerField(null=True)
    isRemote = models.BooleanField(null=True)
    jobType = models.CharField(null=True, max_length=32)
    experience = models.CharField(null=True, max_length=32)
    website = models.CharField(null=True, blank=True, max_length=64)
    websiteIcon = models.ImageField(null=True, blank=True, upload_to='company/logo-social.png')

