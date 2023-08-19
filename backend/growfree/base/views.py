from django.shortcuts import render
from django.http import HttpResponse
from . import models 

# Create your views here.

def index(request):
    return render(request, 'index.html')

def resources(request):
    # context = {
    #     "resources" : models.Opportunity.objects.all(),
    #     "tags": models.Tag.objects.all(),
    #     }
    context = {
    "resources": models.Opportunity.objects.all(),
    "tags": models.Tag.objects.all(),
}
    tags_with_opportunities = []
    for tag in context["tags"]:
        tag_with_opportunities = {
            "tag": tag,
            "opportunities": tag.opportunities.all(),
        }
        tags_with_opportunities.append(tag_with_opportunities)
    context["tags_with_opportunities"] = tags_with_opportunities
    return render(request , "opportunities.html" , context) 


## Form  
def research_help(request):
    pass