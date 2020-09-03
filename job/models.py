from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

def upload_image(instance, file_name):
    _, ext = file_name.split('.')
    return 'jobs/{}.{}'.format(instance.id, ext)

class Job(models.Model):
    JOP_TYPE = (('Full Time','Full Time'),
                ('Part Time','Part Time'),)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
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
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug =='':
            self.slug = slugify(self.title)
        super(Job, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
class Apply(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    portfolio = models.URLField()
    cv = models.FileField(upload_to='cv')
    cover_litter = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
    