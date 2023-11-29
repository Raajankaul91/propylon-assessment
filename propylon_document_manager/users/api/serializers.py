from rest_framework import serializers
from propylon_document_manager.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def to_representation(self, obj):

        return {
            "id": obj.id,
            "name": obj.name,
            "email": obj.email,
        }
