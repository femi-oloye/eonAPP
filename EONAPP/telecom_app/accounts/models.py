from django.db import models
from django.contrib.auth.models import User

class TelemarketData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    dialed_contacts = models.IntegerField()
    connected_calls = models.IntegerField()
    credited_amount = models.DecimalField(max_digits=10, decimal_places=2)
    referred_contacts = models.IntegerField()
    feedback = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s Telemarket Data"
