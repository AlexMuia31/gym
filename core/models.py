from django.db import models

# Create your models here.
PLAN_CHOICES=(
    ('quaterly','quaterly'),
    ('half yearly','half year'),
    ('yearly','yearly')
)

CATEGORY=(
    ('BodyBuilding','BodyBuilding'),
    ('Fitness','Fitness'),
    ('Weight Lifting','Weight Lifting'),
    
)

class User(models.Model):
    plan=models.CharField(choices=PLAN_CHOICES, max_length=12)
    category=models.CharField(choices=CATEGORY, max_length=20)
    picture=models.ImageField(upload_to='images/',null=True, blank=True)
    
    

    def __str__(self):
        return "%s %s" % (self.first_name, self.second_name)

        
class contactModel(models.Model):
    name= models.CharField(max_length=30)
    Email=models.EmailField(max_length=30)
    message=models.TextField(max_length=500)


    def __str__(self):
        return self.name
   

