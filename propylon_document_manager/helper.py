import base64
from base64 import b64decode


# converts base64 format into human readable data and also provies the mode
# in which the file needs to be opened in to store that data
def get_readable_data(base64_encoded_data, file_type):

    base64_text = base64_encoded_data.split("base64,", 1)[1]
    _bytes = b64decode(base64_text, validate=True)
    if _bytes[0:4] != b'%PDF' and file_type=="application/pdf":
        raise ValueError('Missing the PDF file signature')
    elif _bytes[0:4] == b'%PDF' and file_type=="application/pdf":
        return _bytes, "wb"
    elif "image" in file_type:
        return _bytes, "wb"
    elif "officedocument" in file_type:
        return _bytes, "wb"

    readable_data = _bytes.decode('utf-8')
    return readable_data, "w"


# Provides octal permission values for read/write permission enforcement on files
def get_permission_octal_value(is_readable, is_writable):

    if is_readable and not is_writable:
        permission_octal = 0o444
    elif is_writable and not is_readable:
        permission_octal = 0o222
    elif is_readable and is_writable:
        permission_octal = 0o666
    else:
        permission_octal = 0o777

    return permission_octal
