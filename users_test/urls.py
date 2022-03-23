from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name="register"),    # Remember, this route sends people to the register view
                                                                # With the data from the "form" variable in views.py
    # path('', include('blog-urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),   # Built in view
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),    # Built in view
]
