from django.db import models
from datetime import datetime
import os

class UploadFileModel(models.Model):
    file_name = models.CharField(max_length=pow(2,8))#256
    time_stamp = models.DateTimeField(default = datetime.now)