from django.shortcuts import render
from django.http import HttpResponse
from . import models 

# Create your views here.

def index(request):
    return render(request, 'index.html')


def resources(request):
    excluded_tags = []  # Add the names of tags to exclude
    context = {
        "resources": models.Opportunity.objects.all(),
        "tags_with_opportunities": [],
    }

    for tag in models.Tag.objects.exclude(name__in=excluded_tags):
        tag_with_opportunities = {
            "tag": tag,
            "opportunities": tag.opportunities.all(),
        }
        context["tags_with_opportunities"].append(tag_with_opportunities)

    return render(request, "opportunities.html", context)


def opportunity_detail_view(request): 
    return 



## Form  
def research_help(request):
    pass