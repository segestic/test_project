from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Mail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_receiver')
    subject = models.CharField(max_length=100, null=True)
    content = models.TextField(max_length=100, null=True)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("mail_detail", args=(self.pk,))
