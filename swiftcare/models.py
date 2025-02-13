from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.CharField(max_length=100)
    client_password1 = models.CharField(max_length=100)
    client_password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.client_name

