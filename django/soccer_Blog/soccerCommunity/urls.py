from django.contrib import admin
from django.urls import path
from soccerCommunity import views as soccerCommunity_views

urlpatterns = [
    path("<str:id>", soccerCommunity_views.detail, name="detail"),
    path("new/",soccerCommunity_views.new, name="new" ),
    path("create/",soccerCommunity_views.create, name='create'),
    path("edit/<str:id>",soccerCommunity_views.edit,name='edit'),
    path("update/<str:id>",soccerCommunity_views.update, name='update'),
    path("delete/<str:id>",soccerCommunity_views.delete, name='delete'),

]