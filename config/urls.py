
from django.contrib import admin
from analyzer.urls import urls
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
]
