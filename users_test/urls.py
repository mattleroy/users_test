from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name="register"),    # Remember, this route sends people to the register view
                                                                # With the data from the "form" variable in views.py
    # path('', include('blog-urls')),

]
