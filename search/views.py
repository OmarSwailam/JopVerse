from django.shortcuts import render, HttpResponse, redirect
from django.http.response import JsonResponse
from .models import Job
from .serializers import JobSerializer
from .utils import scraper

def search(request):
    if request.method == 'POST':
        jobTitle = request.POST['search']
        jobs = scraper(jobTitle=jobTitle)
        serializer = JobSerializer(data=jobs, many=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('search')

    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return render(request, 'search/search.html', {
        'data': JsonResponse(serializer.data, safe=False)
        })