from django.db import models
import uuid
# Create your models here.

class Competition(models.Model):
    competition_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    competition = models.CharField(max_length=150)
    time = models.TimeField(default=None)
    room_time = models.TimeField(default=None,null=True)
    
    def __str__(self):
        return f"{self.competition_id}"