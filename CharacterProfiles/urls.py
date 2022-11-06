from django.urls import path
from CharacterProfiles import views

app_name = "CharacterProfiles"

urlpatterns = [
    path("addprofile", views.addprofile, name="addprofile"),
    path("getprofiles", views.getprofiles, name="getprofiles"),
    path("editprofile", views.editprofile, name="editprofile"),
    path("deleteprofile", views.deleteprofile, name="deleteprofile"),
]
