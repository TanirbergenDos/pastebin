from django.db import models
from django.urls import reverse
from django.utils.timezone import now



class NotExpiredManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(expired_at__gte=now())


class Paste(models.Model):
    text = models.TextField()
    url = models.CharField(max_length=100, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    objects = models.Manager()
    not_expired = NotExpiredManager()

    def __str__(self):
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text
    
    def get_absolute_url(self):
        return reverse("pastes:show", kwargs={"pk": self.url})
    

   
