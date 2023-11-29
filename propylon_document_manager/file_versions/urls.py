from django.urls import path
from propylon_document_manager.file_versions.api.views import FileVersionList, FileVersionSearch, FileVersion


urlpatterns = [
    path('', FileVersionList.as_view()),
    path('search/', FileVersionSearch.as_view()),
    path('<int:file_version>/', FileVersion.as_view())
]