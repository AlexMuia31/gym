from django.db import models

# Create your models here.
class Blog(models.Model):
    Title= models.CharField(max_length=100,unique=True)
    Body= models.TextField()
    Picture= models.ImageField(upload_to='images/', null=True, blank=True)
    pub_date=models.DateTimeField()
    author=models.CharField(max_length=100)
    


    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.Title
    

    def summary(self):
        return self.Body[:150]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
