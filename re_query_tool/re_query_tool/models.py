from django.core.validators import MinLengthValidator
from django.db import models
import json


class Tool(models.Model):
    string = models.TextField(
        help_text="Write your views", validators=[MinLengthValidator(1)])
    pattern = models.TextField(
        help_text="Enter you regex", validators=[MinLengthValidator(1)])
    match = models.CharField(max_length=255, default=None)
    time_stamp = models.TimeField(auto_now_add=True)
