from django.urls import path
from propylon_document_manager.file_versions.api.views import FileVersionList, FileVersionSearch, FileVersion


urlpatterns = [
    path('', FileVersionList.as_view(), name="file_version_files"),
    path('search/', FileVersionSearch.as_view(), name="file_search"),
    path('<int:file_version>/', FileVersion.as_view(), name="file_version_file")
]