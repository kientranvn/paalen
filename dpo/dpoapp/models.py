from django.db import models
from viewflow.models import Process

class HelloWorldProcess(Process):
    text = models.Charfield(max_length=150)
    approved = models.BooleanField(default=False)

