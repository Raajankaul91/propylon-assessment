from django.test import SimpleTestCase
from django.urls import reverse, resolve
from propylon_document_manager.file_versions.api.views import FileVersionList, FileVersion


class TestUrls(SimpleTestCase):

    def test_file_version_resolves(self):
        url = reverse("file_version_files")
        self.assertEqual(resolve(url).func.view_class, FileVersionList)

    def test_file_version_file_resolves(self):
        url = reverse("file_version_file", args=[2])
        self.assertEqual(resolve(url).func.view_class, FileVersion)