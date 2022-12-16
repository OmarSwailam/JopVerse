from django.shortcuts import render
from django.http.response import JsonResponse
from django.core import serializers
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from .utils import scraper
from django.http import HttpResponse
from django.db.models import Q


def index(request):
    return render(request, 'search/index.html')


def search(request, q):

    jobs = scraper(jobTitle=q)
    for job in jobs:
        print(job['jobTitle'])
        print(job['jobUrl'])
        print(job['companyName'])
        try:
            obj = Job.objects.get(
                jobUrl=job['jobUrl'],
                )

        except Job.DoesNotExist:
            print('there')
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

    data = Job.objects.distinct().filter(Q(jobTitle__icontains=q))
    response = list(data.values())
    json = JsonResponse(response, safe=False)
    return HttpResponse(json)