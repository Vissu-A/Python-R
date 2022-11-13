from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid


class uregister(AbstractBaseUser):
    uid = models.UUIDField(primary_key=True,default=uuid.uuid4)
    uname = models.CharField(max_length=107)
    passcode = models.CharField(max_length=37)
    role = models.CharField(max_length=37)
    fname = models.CharField(max_length=37)
    lname = models.CharField(max_length=37)
    phoneno = models.IntegerField()
    email = models.EmailField(max_length=37)

    def __str__(self):
        return self.uname

class branch(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    brname = models.CharField(max_length=37)

class bookdetails(models.Model):
    bid = models.UUIDField(primary_key=True,default=uuid.uuid4)
    bname = models.CharField(max_length=37)
    bauthor = models.CharField(max_length=37)
    branchid = models.ForeignKey(branch, on_delete=models.CASCADE)
    avail = models.CharField(max_length=27)

    def __str__(self):
        return self.bname,self.bauthor,self.avail

class takenbooks(models.Model):
    uid = models.ForeignKey(uregister, on_delete=models.CASCADE)
    bid = models.ForeignKey(bookdetails, on_delete=models.CASCADE)
