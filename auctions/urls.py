from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    
    path("watchlist", views.my_watchlist, name='mywatchlist'),
    path("listing/<int:listing_id>/watchlist", views.watchlist, name='watchlist'),
    
    path("close_auction/<int:idd>", views.close_auction, name='close_auction'),

]