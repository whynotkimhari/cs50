from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("wiki/<str:name>", views.getContent, name="encyclopedia"),
    path("create", views.create, name="create"),
    path("save", views.save, name="save"),
    path("editContent", views.editContent, name="editContent"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("randomPage", views.randomPage, name="randomPage"),
]
