from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True)
    isbn = models.BigIntegerField(null=True)
    publisher = models.CharField(max_length=255, null=True)
    status = models.BooleanField(default=True)
    holder = models.IntegerField(null=True)

class Member(models.Model):
    name = models.CharField(max_length = 20)
    number = models.BigIntegerField()
    holding = models.ForeignKey(Books, on_delete=models.RESTRICT, null=True)
    fees = models.IntegerField(default=0)

class Transaction(models.Model):
    member = models.ForeignKey(Member, on_delete=models.RESTRICT)
    book = models.ForeignKey(Books, on_delete=models.RESTRICT)
    type = models.CharField(max_length=10, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)

