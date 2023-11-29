# from propylon_document_manager.file_versions.models import FileVersion
# from django.test import TestCase
#
#
# class TestModels(TestCase):
#
#     def setUp(self):
#         pass
#
#     def test_FileVersion(self):
#
#         obj = {
#             "id": 1,
#             "file_name": "test_name",
#             "version_number": 1,
#             "user_id": 1,
#             "location": ["test", "location"],
#             "file_data": "qwertyuiopasdfghjklzxcvbnm",
#             "file_type": "test/fileType",
#             "is_readable": True,
#             "is_writable": True,
#             "cas_location": "0rf/5fj/3456yg87ytfty6trefgyg"
#         }
#
#         response = FileVersion.objects.create(
#             file_name=obj.get("file_name"),
#             version_number=obj.get("version_number"),
#             user_id=obj.get("user_id"),
#             location=obj.get("location"),
#             file_data=obj.get("file_data"),
#             file_type=obj.get("file_type"),
#             is_readable=obj.get("is_readable"),
#             is_writable=obj.get("is_writable"),
#             cas_location=obj.get("cas_location")
#         )
#
#         self.assertEqual(obj.get("file_name"), response.file_name)

