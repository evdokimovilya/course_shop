from django.contrib import admin

from . models import * 


class LectureInline(admin.StackedInline):
    model = Lecture
    fields = ('title', 'description')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [
        LectureInline,
    ]


class LectureMaterialnline(admin.StackedInline):
    model = LectureMaterial
    fields = ('title', 'type', 'order', 'file', 'text')


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_filter = ('course__title', )
    inlines = [
        LectureMaterialnline,
    ]

admin.site.register(LectureMaterial)
admin.site.register(CourseCategory)



