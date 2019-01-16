from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import JobForm
from .models import Job


def create_job(request):
    job_form = JobForm
    if request.method == "POST":
        job_form = job_form(request.POST)
        if job_form.is_valid():
            job_form.save()
            messages.success(request, message="Job created successfully.")
            return redirect(reverse("list-jobs"))
    return render(request, "jobs/create_job.html", {"form": job_form})

def list_jobs(request):
    if request.method == "GET":
        return render(
            request, "jobs/list_jobs.html", {"jobs": Job.objects.all()}
        )