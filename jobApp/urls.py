from django.urls import path
from . import views

urlpatterns = [
    path('post_job/', views.post_job_view, name='post_job'),
    path('job_listings/', views.job_listings_view, name='job_listings'),
]
