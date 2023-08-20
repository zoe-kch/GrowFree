from django.urls import path 
from . import views 

urlpatterns = [
    path(''  , views.index , name="index"), 
    path('resources' , views.resources, name="resources"), 
    path('research_help' , views.research_help , name="research_help"), 
    path('filtered/<str:tag_name>/', views.resources_filter_by_tag, name='filtered_opportunities'),
    path('academics' , views.academic_screen, name="academics"),
    path('finance' , views.finance , name="finance")

]