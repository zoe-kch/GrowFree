from django.db import models


status_choices = (
        ("active" , "active"),
        ("inactive" , "inactive")
    )

    
    
class Tag(models.Model): 
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.name)
class Opportunity(models.Model): 
    name = models.CharField(max_length=200) 
    description =  models.CharField(max_length=1000)
    url = models.URLField()
    deadline = models.DateField((""), auto_now=False, auto_now_add=False)
    status = models.CharField(
        max_length=100, 
        choices=status_choices, 
        default="active"
    )   
    tags = models.ManyToManyField(Tag , blank=True ,related_name='opportunities') 

    

    
    def __str__(self) -> str:
        return str(self.name)

