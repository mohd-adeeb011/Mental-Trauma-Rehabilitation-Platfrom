from django.contrib import admin
from django.urls import path , include
from home import views

admin.site.site_header = "Team P_Addiction Admin"
admin.site.site_title = "Team P_Addiction Admin Portal"
admin.site.index_title = "Welcome to Team P_Addiction Researcher Portal"

urlpatterns = [
    
    path("",views.index,name="home"),
    path("index",views.index,name="home"),
    path("about",views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("services",views.services,name="services"),
    path("newpage",views.newpage,name="newpage")
] 