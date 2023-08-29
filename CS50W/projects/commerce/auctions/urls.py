from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("bid/<int:id>", views.bid, name="bid"),
    path("close/<int:id>", views.close, name="close"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("addtowatchlist", views.addtowatchlist, name="addtowatchlist"),
    path("removefromwatchlist", views.removefromwatchlist, name="removefromwatchlist"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:name>", views.category, name="category"),
    path("comment", views.comment, name="comment"),
]
