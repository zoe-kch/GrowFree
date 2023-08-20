from django.db import models

college_resource_type = ( 
    ("academics" , "academics") , 
    ("finance" , "finance") 
)

college_resource_topic = ( 
    ("School_Before_College" , "School_Before_College"), 
    ("Searching_for_Colleges", "Searching_for_Colleges"), 
    ("Exam_Prep" , "Exam_Prep"), 
    ("College_Application" , "College_Application"), 
    ("Research" , "Research"), 
    ("Mentors" , "Mentors"), 
    ("Extracurriculars" , "Extracurriculars"), 
    ("Navigating_Scholarships" , "Navigating_Scholarships"), 
    ("Financial_Aid" , "Financial_Aid"), 
    ("Sponsors" , "Sponsors"),
    ("Financial_Literacy_Courses" , "Financial_Literacy_Courses"), 
    ("Additional_resources" , "Additional_resources")

)




status_choices = (
        ("active" , "active"),
        ("inactive" , "inactive")
    )

research_help_choices = (
    ("mentor" , "mentor") , 
    ("student" , "student"), 
    ("study-group"  , "study-group"),
    ('research' , 'research') , 
    ('other' , 'other')
    
    
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
    name= models.CharField(max_length=50, blank=False)
    
    def __str__(self) -> str:
        return str(self.name)

    
class Research_help(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False, unique=True)
    help_type = models.CharField(max_length=100 , choices=research_help_choices , blank=False)
    interests = models.ManyToManyField(Interest , blank=False , related_name='helpers')
    # mapped_users = models.


    def __str__(self) -> str:
        return str(self.name)     
    

class college_help(models.Model): 
    name = models.CharField(max_length=300) 
    url = models.URLField()
    resource_type = models.CharField(max_length=100 , choices=college_resource_type)
    topic = models.CharField(max_length=200 , choices=college_resource_topic)


    def __str__(self) -> str:
        return str(self.name)