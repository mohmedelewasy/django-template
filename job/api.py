from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs, many = True).data
    return Response({'data': data})
 
@api_view(['GET'])
def job_detail_api(request, slug):
    job = Job.objects.get(slug = slug)
    data = JobSerializer(job).data
    return Response({'data': data})

#CBV
class JobListApi(generics.ListAPIView):
    model = Job
    queryset = Job.objects.all()
    serializer_class = JobSerializer