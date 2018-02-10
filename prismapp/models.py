from django.db import models
from datetime import datetime
import os

class UploadFileModel(models.Model):
    ori_file_name = models.CharField(max_length=pow(2,8))#256
    re_file_name = models.CharField(max_length=pow(2,8))#256
    file = models.FileField(upload_to="files/")
    time_stamp = models.DateTimeField(default = datetime.now)

    def get_filename(self):
        return os.path.basename(self.file.name)