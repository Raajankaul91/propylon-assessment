from django.urls import re_path, include


urlpatterns = [
    re_path('file_versions/', include('file_versions.urls')),
    re_path('users/', include('users.urls'))
]
