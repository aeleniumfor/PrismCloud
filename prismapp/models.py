from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import os


def user_directory_path(instance, filename):

    return 'files/user_{0}/{1}'.format(instance.user.id, filename)


class UploadFileModel(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    ori_file_name = models.CharField(max_length=pow(2, 8))  # 256
    re_file_name = models.CharField(max_length=pow(2, 8))  # 256
    file = models.FileField(upload_to=user_directory_path)
    time_stamp = models.DateTimeField(default=datetime.now)

    def get_filename(self):
        return os.path.basename(self.file.name)
