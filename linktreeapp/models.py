from django.db import models

# Create your models here.
class Userdetails(models.Model):
    uemail = models.CharField(max_length=100, null=False)
    usname = models.CharField(max_length=100, null=True)
    desg = models.CharField(max_length=100, null=True)
    port = models.CharField(max_length=100)
    res = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    linked = models.CharField(max_length=100)
    insta = models.CharField(max_length=100)
    fb = models.CharField(max_length=100)
    hack = models.CharField(max_length=100)
    codechef = models.CharField(max_length=100)
    leet = models.CharField(max_length=100)
    gthub = models.CharField(max_length=100)
    gfg = models.CharField(max_length=100)

    def __str__(self):
        return f"({self.uemail})"
