from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('', include('users.urls')), # INCLUDE FRONT PAGE HERE
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name="register"),    # Remember, this route sends people to the register view with the data from the "form" variable in views.py
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),   # Built in view
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),    # Built in view
    # Remember, the 4 views above, (except the empty string) are all views that already have been written (By Django).
    # So writing views in users.views for these URL path's isn't needed
]