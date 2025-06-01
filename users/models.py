from django.db import models

# Create your models here.
class Plan(models.Model):
    measure = models.CharField(max_length=50)
    about = models.TextField( )
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.about
    
    