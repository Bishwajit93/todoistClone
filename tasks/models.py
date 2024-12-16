from django.db import models

# Create your models here.
class TASK(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField((""))
    created_at = models.DateTimeField(auto_now_add=True)
    comleted = models.BooleanField(default = False)
    
    
    def __str__(self):
        return self.title