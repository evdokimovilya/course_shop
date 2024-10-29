from django.db import models


class CourseCategory(models.Model):
    title = models.CharField(max_length=255)  

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


    def __str__(self) -> str:
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)   
    description = models.TextField()
    price = models.IntegerField()
    free = models.BooleanField(default=False)
    image = models.FileField(null=True, blank=True, upload_to='media/')
    category = models.ForeignKey(CourseCategory, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Курсы"
        verbose_name_plural = "Курсы"

    def __str__(self) -> str:
        return self.title
    
    # def not_in_basket(self):
    #     return settinf
    
class Lecture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, related_name='course_lectures', on_delete=models.CASCADE)
    order = models.IntegerField(default=0) 

    class Meta:
        verbose_name = "Лекция"
        verbose_name_plural = "Лекции"
        ordering = ['order', ]

    def __str__(self) -> str:
        return self.title


class LectureMaterial(models.Model):
    class MaterialType(models.TextChoices):
        TEXT = "Text"
        VIDEO = "Video"
        IMAGE = 'Image'
    title = models.CharField(max_length=255)
    type = models.CharField(choices=MaterialType, max_length=10)
    order = models.IntegerField(default=0)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='lecture_materials')
    file = models.FileField(null=True, blank=True)
    text = models.TextField(blank=True)

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
        ordering = ['order', ]

    def __str__(self) -> str:
        return self.title

