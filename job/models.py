from django.db import models

def upload_image(instance, file_name):
    _, ext = file_name.split('.')
    return 'jobs/{}.{}'.format(instance.id, ext)

class Job(models.Model):
    JOP_TYPE = (('Full Time','Full Time'),
                ('Part Time','Part Time'),)
    
    title = models.CharField(max_length=100)
    #location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, choices = JOP_TYPE)
    description = models.TextField(max_length=2000) 
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    image = models.ImageField(upload_to=upload_image)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
    