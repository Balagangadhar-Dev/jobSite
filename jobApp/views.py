from django.shortcuts import render, redirect
from .models import JobPost
# Create your views here.


def post_job_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        company_name = request.POST.get('company_name')
        location = request.POST.get('location')
        description = request.POST.get('description')

        job_post = JobPost.objects.create(
            title=title,
            company_name=company_name,
            location=location,
            description=description
        )
        return redirect('job_listings')
    return render(request, 'post_job.html')

def job_listings_view(request):
    job_posts = JobPost.objects.all()
    return render(request, 'job_listings.html', {'job_posts': job_posts})
