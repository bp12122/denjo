from django.db import models
from django.db.models.fields import DateTimeField, TextField


class Hope(models.Model):
    number_of_people = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    place = models.CharField(max_length=30)
    date_and_time = models.DateTimeField('hope datetime')
    pub_date_and_time = models.DateTimeField(auto_now_add=True)
    memo = models.TextField(null=True, blank=True)
    customer_user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    class Meta:
        db_table = 'hopes'

"""
class Suggestion(models.Model):
    number_of_people = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    place = models.CharField(max_length=30)
    date_and_time = models.DateTimeField('suggestion datetime')
    pub_date_and_time = models.DateTimeField(auto_now_add=True)
    memo = models.TextField(null=True, blank=True)
    auto_flag = models.BooleanField(default=0)
    hope = models.ForeignKey("microposts.Hope", on_delete=models.CASCADE)
    shop = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.shop.username

class Reserve(models.Model):
    suggestion = models.ForeignKey("microposts.Suggestion", on_delete=models.CASCADE)

    def __str__(self):
        return self.suggestion.hope.customer_user.username + ',' + self.suggestion.shop.username

class Course(models.Model):
    shop = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    time = models.TimeField()
    price = models.IntegerField(default=0)
    memo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.shop.username + '(' + self.title + ')'

class Orderunit(models.Model):
    shop = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    course = models.ForeignKey("microposts.Course", null=True, on_delete=models.SET_NULL, blank=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    memo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.shop.username + '(' + self.name + ')'
"""