from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm, AddJobForm
from django.contrib.auth.decorators import login_required

def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            form = ApplyForm()
        
    else:
        form = ApplyForm()
    
    context = {'job': job_detail, 'form': form}
    return render(request, 'job/job_details.html', context)

def job_list(request):
    job_list = Job.objects.all()
    
    paginator = Paginator(job_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs': job_list, 'paginator': page_obj}
    return render(request, 'job/jobs.html', context)

@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit = False)
            myform.owner = request.user
            myform.save()
            form = AddJobForm()
    else:
        form = AddJobForm()
    context = {'form': form}
    return render(request, 'job/add_job.html', context)