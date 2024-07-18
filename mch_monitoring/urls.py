from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/surveyors/', include('surveyors.urls')),
    path('api/mothers/', include('mothers.urls')),
    path('api/children/', include('children.urls')),
    path('users/', include('accounts.urls')),
]
