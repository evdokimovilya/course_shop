from django.db import models

from django.contrib.auth.models import User
from apps.course.models import Course

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)


    def get_courses(self):
        return [course_profile.course for course_profile in self.profile_courses.all()]
    

class CourseProfile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
 