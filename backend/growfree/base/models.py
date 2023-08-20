from django.db import models


status_choices = (
        ("active" , "active"),
        ("inactive" , "inactive")
    )

research_help_choices = (
    ("mentor" , "mentor") , 
    ("student" , "student"), 
    ("studygroup"  , "studygroup"), 
    
)
    
    
class Tag(models.Model): 
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.name)
class Opportunity(models.Model): 
    name = models.CharField(max_length=200) 
    description =  models.CharField(max_length=1000, blank=True)
    url = models.URLField()
    deadline = models.DateField((""), auto_now=False, auto_now_add=False)
    status = models.CharField(
        max_length=100, 
        choices=status_choices, 
        default="active"
    )   
    tags = models.ManyToManyField(Tag , blank=True ,related_name='opportunities') 

    

    
    def __str__(self) -> str:
        return str(self.name) + " || " +  str(self.tags.name) + " || " + str(self.deadline)

class Interest(models.Model): 
    name= models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return str(self.name)

    
class Research_help(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    help_type = models.CharField(max_length=100 , choices=research_help_choices , blank=False)
    interests = models.ManyToManyField(Interest , blank=False , related_name='helpers')

    def __str__(self) -> str:
        return str(self.name)     
    

    