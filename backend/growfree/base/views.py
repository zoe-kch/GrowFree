from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models 
from django.urls import reverse

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


## Form  
def research_help(request):
    if request.method == "POST": 
        email = request.POST["Email"]
        name = request.POST["Name"]
        interests_names = request.POST.getlist("interests")
        help_type = request.POST["connections"]

        if len(interests_names) > 1: 
            interests = [models.Interest.objects.get_or_create(name=interest)[0] for interest in interests_names ]  
        else: 
            interests = models.Interest.objects.get_or_create(name=interests_names[0])
        

        research_helper = models.Research_help.objects.create(name=name , email=email , help_type=help_type)
        research_helper.interests.add(*interests)

        return HttpResponseRedirect(reverse('index'))
    
