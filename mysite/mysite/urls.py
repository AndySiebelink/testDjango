from django.contrib import admin
from django.urls import path, include  # ← include toegevoegd

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
