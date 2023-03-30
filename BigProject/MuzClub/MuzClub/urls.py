"""MuzClub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views as app_views
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.main_page, name='home'),
    path('songs/', app_views.song_list, name='songs'),
    path('songs/<int:pk>', app_views.song_detail_view.as_view(), name='song'),
    path('songs/delete/<int:pk>', app_views.song_delete, name='song_delete'),
    path('songs/create/', app_views.song_create, name='song_create'),
    path('songs/like/<int:pk>', user_views.like_song, name='like_song'),
    path('songs/search/', app_views.search_something, name='search_result'),

    path('songs/categories', app_views.genres_list_view.as_view(), name='genres'),
    path('songs/categories/create', app_views.genre_create_view.as_view(), name='genres_create'),
    path('songs/categories/delete/<int:pk>', app_views.genre_delete, name='delete_category'),
    path('songs/categories/<int:pk>', app_views.genre_detail, name='current_category'),




    path('users/create', user_views.registration_view.as_view(), name='user_registration'),
    path('users/login', user_views.user_login_view.as_view(), name='user_login'),
    path('users/logout', user_views.user_logout_view.as_view(), name='user_logout'),
    path('users/profile/', user_views.user_profile.as_view(), name='user_profile'),
    path('users/playlist/', user_views.playlist.as_view(), name='user_playlist'),
    path('users/playlist/delete/<int:pk>', user_views.delete_from_playlist, name='user_playlist_delete'),
    path('users/<str:name>', user_views.other_user.as_view(), name='other_user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = app_views.page_not_found
handler500 = app_views.handler500

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)