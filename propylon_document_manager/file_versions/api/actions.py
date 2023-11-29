import hashlib
from pathlib import Path
from file_versions.models import FileVersion, FileData
from propylon_document_manager.helper import *
from django.db.models import Max
import os
import traceback
from django.db.utils import IntegrityError


class DoesNotExistsException(Exception):
    pass


def get_files(user_id):

    files = FileVersion.objects.filter(user_id=user_id)
    return files


def add_file(user_id, file):

    file_name = file.get("file_name")
    location = file.get("location")
    file_data = file.get("file_data")
    file_type = file.get("file_type")
    is_readable = file.get("is_readable", False)
    is_writable = file.get("is_writable", False)

    readable_data, file_open_mode = get_readable_data(file_data, file_type)

    digest = hashlib.sha1(str(readable_data).encode()).hexdigest()
    cas_location = digest[:3] + "/" + digest[3:6] + "/" + digest[6:]

    current_dir = os.path.abspath(os.getcwd())
    path = current_dir + "/media/" + cas_location
    Path(path).mkdir(parents=True, exist_ok=True)

    file_data_id = FileData.objects.get_or_create(file_data=file_data, cas_location=cas_location)

    try:
        version_number = get_version(file, file_data_id[0].id)
    except IntegrityError as error:
        raise IntegrityError(error)

    file = FileVersion.objects.create(file_name=file_name, location=location, user_id=user_id,
                                      version_number=version_number, file_data_id=file_data_id[0].id,
                                      file_type=file_type, is_readable=is_readable, is_writable=is_writable)

    permissions = get_permission_octal_value(is_readable, is_writable)
    with open(os.path.join(path, file_name), file_open_mode) as f:
        f.write(readable_data)

    os.chmod(os.path.join(path, file_name), permissions)

    return file


def get_version(file, file_data_id):

    version = 0

    location = file.get("location")
    file_name = file.get("file_name")
    try:
        has_duplicate_entry = FileVersion.objects.get(location=location, file_name=file_name, file_data_id=file_data_id)
    except FileVersion.DoesNotExist:
        has_duplicate_entry = None

    if has_duplicate_entry:
        raise IntegrityError("Duplicate entry! file save canceled.")

    file = FileVersion.objects.filter(location=location, file_name=file_name)

    if len(file) != 0:
        version = file.aggregate(Max('version_number'))["version_number__max"] + 1

    return version


def search_files(user_id, search_value):

    filtered_files = []
    valid_file_type = ["text/plain", "text/rtf"]

    files = FileVersion.objects.filter(user_id=user_id, file_type__in=valid_file_type)

    for file in files:
        text = get_readable_data(file.file_data.file_data, file.file_type)

        if search_value in text:
            filtered_files.append(file)
        else:
            continue

    return filtered_files


def get_file(params, version_number):

    file_name = params.get("file_name")
    location = params.get("location").split(",")
    location = '/'.join(location)
    try:
        file = FileVersion.objects.get(file_name=file_name, version_number=version_number, location=location)
    except FileVersion.DoesNotExist:
        raise Exception("File not found.")

    return file









