from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models 
from django.urls import reverse
from itertools import combinations
from collections import defaultdict


## HELPER FUNCTIONS from .models import Research_help

def map_users_by_interest(user_name):
    # Retrieve the user's interests
    user_interests = set()
    user_helpers = models.Research_help.objects.filter(name=user_name).first()
    if user_helpers:
        user_interests = set(user_helpers.interests.all())

    # Create a dictionary to store other users based on shared interests
    user_interest_mapping = {}
    all_helpers = models.Research_help.objects.exclude(name=user_name)  # Exclude the current user
    for helper in all_helpers:
        common_interests = set(helper.interests.all()) & user_interests
        if common_interests:
            user_interest_mapping[helper.name] = common_interests
            
    return user_interest_mapping










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

        if "@" in email and len(name) > 2 and interests_names and help_type: 

            if len(interests_names) > 1: 
                interests = [models.Interest.objects.get_or_create(name=interest)[0] for interest in interests_names ]  
                research_helper = models.Research_help.objects.create(name=name , email=email , help_type=help_type)
                research_helper.interests.add(*interests)
            else: 
                interests = models.Interest.objects.get_or_create(name=interests_names[0])[0]

                research_helper = models.Research_help.objects.create(name=name , email=email , help_type=help_type)

                research_helper.interests.add(interests)

        # Provide the user's name
            user_name = name  # Replace with the desired user's name
            user_mapping = map_users_by_interest(user_name)

            print(user_mapping)

        return HttpResponseRedirect(reverse('index'))

    else: 
        ## ADD ERROR MSG 
        return HttpResponseRedirect(reverse(index))
    



    
