from django.db import models

# Create your models here.
class Blog(models.Model):
    Title= models.CharField(max_length=100)
    Body= models.TextField()
    Picture= models.ImageField(upload_to='images/', null=True, blank=True)
    pub_date=models.DateTimeField()


    def __str__(self):
        return self.Title
    

    def summary(self):
        return self.Body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')