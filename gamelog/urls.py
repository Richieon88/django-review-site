from django.contrib import admin
from django.urls import path, include
from gamelog.views import homepage
from django.contrib.auth import views as auth_views
from accounts.views import register
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('games/', include(('games.urls', 'games'), namespace='games')),
    path('reviews/', include(('reviews.urls', 'reviews'), namespace='reviews')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/register/', register, name='register'),
]
