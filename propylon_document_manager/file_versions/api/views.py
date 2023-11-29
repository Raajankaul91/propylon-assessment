from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from propylon_document_manager.scope import Scopes, ScopeException
from propylon_document_manager.file_versions.api.actions import *
from .serializers import FileVersionSerializer
from rest_framework import status


class FileVersionList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        user_id = request.user.id

        files = get_files(user_id)

        serialized_files = FileVersionSerializer(files, many=True).data
        return Response({"files": serialized_files}, status=200)

    def post(self, request):

        user_id = request.user.id
        file = request.data

        try:
            file = add_file(user_id, file)
        except IntegrityError as error:
            return Response({'message': str(error)}, status=status.HTTP_409_CONFLICT)

        serialized_file = FileVersionSerializer(file, many=False).data
        return Response({"file": serialized_file}, status=200)


class FileVersionSearch(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        user_id = request.user.id
        params = request.query_params

        search_value = params.get('search_value', None)

        files = search_files(user_id, search_value)

        serialized_files = FileVersionSerializer(files, many=True).data
        return Response({"files": serialized_files}, status=200)


class FileVersion(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, file_version):

        user_id = request.user.id
        params = request.query_params

        try:
            file = get_file(params, file_version)
        except Exception as error:
            return Response({'message': str(error)}, status=status.HTTP_404_NOT_FOUND)

        serialized_file = FileVersionSerializer(file, many=False).data

        # Checking the scope of the user: Checking if the user ownes the file he is trying to access
        try:
            Scopes.in_user_scope(user_id, file_user_id=serialized_file['user_id'])
        except ScopeException as error:
            return Response({ 'message': str(error) }, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"file": serialized_file}, status=200)

