from django.db import models

# Create your models here.

class post(models.Model):
    author  = models.ForeignKey(user , on_delete=models.CASCADE)
    image = models.ImageField(null=True , blank=True)
    title = models.CharField(max_length=220)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('category' ,on_delete= models.SET_NULL,null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class category(models.Model):
    name = models.CharField(max_length=220)

    def __str__(self):
        return self.name
