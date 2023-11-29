from django.urls import path
from propylon_document_manager.users.api.views import UserViewSet
from propylon_document_manager.file_versions.api.views import FileVersionList, FileVersionSearch, FileVersion


urlpatterns = [
    path('file_versions/', FileVersionList.as_view()),
    path('file_versions/search/', FileVersionSearch.as_view()),
    path('file_versions/<int:file_version>/', FileVersion.as_view())
]
