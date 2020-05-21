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
    ('Boxing','Boxing')
)

class User(models.Model):
    first_name= models.CharField(max_length= 200)
    second_name=models.CharField(max_length=200)
    plan=models.CharField(choices=PLAN_CHOICES, max_length=12)
    category=models.CharField(choices=CATEGORY, max_length=20)
    picture=models.ImageField(upload_to='images/',null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.second_name)

        



    

