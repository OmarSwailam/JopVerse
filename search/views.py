from django.shortcuts import render
from django.http.response import JsonResponse
from django.core import serializers
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from .utils import scraper
from django.http import HttpResponse

def search(request):
    jobTitle = ''
    if request.GET.get('q'):
        jobTitle = request.GET.get('q')
        jobs = scraper(jobTitle=jobTitle)
        for job in jobs:
            try:
                obj = Job.objects.get(
                    jobTitle=job['jobTitle'],
                    jobUrl=job['jobUrl'],
                    companyName=job['companyName'],
                    companyImage=job['companyImage'],
                    salary=job['salary'],
                    isRemote=job['isRemote'],
                    jobType=job['jobType'],
                    experience=job['experience'],
                    website=job['website'],
                    websiteIcon=job['websiteIcon'],
                    )
            except Job.DoesNotExist:
                obj = Job(
                    jobTitle=job['jobTitle'],
                    jobUrl=job['jobUrl'],
                    companyName=job['companyName'],
                    companyImage=job['companyImage'],
                    salary=job['salary'],
                    isRemote=job['isRemote'],
                    jobType=job['jobType'],
                    experience=job['experience'],
                    website=job['website'],
                    websiteIcon=job['websiteIcon'],
                    )
                obj.save()

    data = Job.objects.filter(jobTitle__icontains=jobTitle)
    response = list(data.values())
    json = JsonResponse(response, safe=False)
    return json