from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.contrib.auth import get_user_model
from embed_video.fields import EmbedVideoField



class User(AbstractUser):
    is_learner = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = '', default = 'no-img.jpg', blank=True)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(default='none@email.com')
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(default='1975-12-12')
    bio = models.TextField(default='')
    city = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    country = models.CharField(max_length=255, default='')
    favorite_animal = models.CharField(max_length=255, default='')
    hobby = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.user.username



class Course(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')


    def __str__(self):
        return self.name


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    interest = models.ManyToManyField(Course, related_name="interested_instructors")

    def __str__(self):
        return self.user.username


class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='announcements', null=True, blank=True)
    posted_at = models.DateTimeField(auto_now=True, null=True)
    meeting = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.content)

    def get_html_badge(self):
        if self.course:
            name = escape(self.course.name)
            color = escape(self.course.color)
            html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
            return mark_safe(html)
        else:
            return ''




class Tutorial(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    thumb = models.ImageField(upload_to='', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = EmbedVideoField(blank=True, null=True)


class Notes(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to='', null=True, blank=True)
    cover = models.ImageField(upload_to='', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)    






class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    interests = models.ManyToManyField(Course, related_name='interested_learners')


    def __str__(self):
        return self.user.username





