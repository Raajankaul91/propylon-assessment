from django.db import models
from propylon_document_manager.users.models import User
import datetime
import pytz


class FileData(models.Model):
    file_data = models.TextField()
    cas_location = models.fields.CharField(max_length=100, unique=True, default="000/000/000")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
        super(FileData, self).save(*args, **kwargs)

    class Meta:
        app_label = "file_versions"
        ordering = ('created_at',)


class FileVersion(models.Model):
    file_name = models.fields.CharField(max_length=512)
    file_type = models.fields.CharField(max_length=512)
    version_number = models.fields.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_data = models.ForeignKey(FileData, on_delete=models.CASCADE)
    location = models.fields.CharField(max_length=512, default="defaultFolder")
    is_readable = models.fields.BooleanField(default=False)
    is_writable = models.fields.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
        super(FileVersion, self).save(*args, **kwargs)

    def __str__(self):
        return self.file_name

    class Meta:
        app_label = "file_versions"
        ordering = ('created_at',)
