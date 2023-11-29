from rest_framework import serializers
from file_versions.models import FileVersion


class FileVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileVersion
        fields = "__all__"

    def to_representation(self, obj):

        return {
            "id": obj.id,
            "file_name": obj.file_name,
            "version_number": obj.version_number,
            "user_id": obj.user.id,
            "location": obj.location.split("/"),
            "file_data": obj.file_data.file_data,
            "file_type": obj.file_type,
            "is_readable": obj.is_readable,
            "is_writable": obj.is_writable,
            "cas_location": obj.file_data.cas_location
        }
