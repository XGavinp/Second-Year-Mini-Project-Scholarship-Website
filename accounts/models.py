from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    forget_password_token = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Gender(models.Model):
    gender = models.TextField(max_length=20)

    def __str__(self):
        return self.gender


class Education(models.Model):
    education = models.TextField(max_length=100)

    def __str__(self):
        return (self.education)

class Course(models.Model):
    course_name = models.TextField(max_length=200)

    def __str__(self):
        return (self.course_name)

class Eligibility(models.Model):
    body = models.TextField(max_length=600)

    def __str__(self):
        return (self.body[0:50])

class Location(models.Model):
    location = models.TextField(max_length=30)

    def __str__(self):
        return (self.location) 

class Major(models.Model):
    major_name = models.TextField(max_length=100)

    def __str__(self):
        return super(self.major_name)  

class Language(models.Model):
    language = models.CharField(max_length=20)

    def __str__(self):
        return (self.language)
    
class Accomodation(models.Model):
    ans = models.CharField(max_length=3)

    def __str__(self):
        return (self.ans)
    
class Living_Expense(models.Model):
    ans = models.CharField(max_length=3)

    def __str__(self):
        return (self.ans)

class Month(models.Model):
    month = models.CharField(max_length=20)

    def __str__(self):
        return (self.month)
    
class Year(models.Model):
    year = models.CharField(max_length=10)

    def __str__(self):
        return (self.year)

class Key(models.Model):
    key = models.TextField()

    def __str__(self):
        return (self)

class Level(models.Model):
    level = models.TextField(max_length=100)

    def __str__(self):
        return (self.level)

class Scholarship(models.Model):
    host = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default='admin')
    uni_name = models.TextField(max_length=250, null=True)
    major = models.ForeignKey(Major, null=True, on_delete=models.SET_NULL)
    key = models.ForeignKey(Key, null=True, on_delete=models.SET_NULL)
    level = models.ForeignKey(Level, null=True, on_delete=models.SET_NULL)
    language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    tuition_covered = models.FloatField(max_length=10, null=True)
    accomodation = models.ForeignKey(Accomodation, null=True, on_delete=models.SET_NULL)
    living = models.ForeignKey(Living_Expense, null=True, on_delete=models.SET_NULL)
    to_be_paid_tuition = models.FloatField(max_length=10, null=True)
    per_sch = models.FloatField(max_length=100, null=True)
    org_tuition = models.FloatField(max_length=10, null=True)
    month = models.ForeignKey(Month, null=True, on_delete=models.SET_NULL)
    year = models.ForeignKey(Year, null=True, on_delete=models.SET_NULL)
    amt_accomodation = models.FloatField(null=True)
    amt_living = models.FloatField(null=True)
    
    
    '''@property
    def Days_till(self):
        today = date.today()
        days_till = self.last_date.date() - today
        days_till_stripped = str(days_till).split("," , 1)[0]
        return days_till_stripped'''

    def __str__(self):
        return self.uni_name[0:10]
    
class s_data(models.Model):
    host = models.TextField(null=True, default='admin')
    uni_name = models.TextField(max_length=250, null=True)
    major = models.TextField(null=True)
    key = models.TextField(null=True)
    level = models.CharField(max_length=12)
    language = models.TextField(null=True)
    tuition_covered = models.FloatField(max_length=10, null=True)
    accomodation = models.CharField(max_length=3, null=True)
    living = models.CharField(max_length=3, null=True)
    to_be_paid_tuition = models.FloatField(max_length=10, null=True)
    per_sch = models.FloatField(max_length=100, null=True)
    org_tuition = models.FloatField(max_length=10, null=True)
    month = models.TextField(null=True)
    year = models.IntegerField(null=True)
    amt_accomodation = models.FloatField(null=True)
    amt_living = models.FloatField(null=True)
    
    
    '''@property
    def Days_till(self):
        today = date.today()
        days_till = self.last_date.date() - today
        days_till_stripped = str(days_till).split("," , 1)[0]
        return days_till_stripped'''

    def __str__(self):
        return self.uni_name[0:10]