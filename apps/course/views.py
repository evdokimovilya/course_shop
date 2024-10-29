from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from .models import Course, CourseCategory


def course_list(request): 

    context = {}

    courses = Course.objects.all()
    categories = CourseCategory.objects.all()

    category_filter = request.GET.get('category')
    active_category = None

    try:
        category = CourseCategory.objects.get(id=category_filter)
        courses = courses.filter(category=category)
        active_category = category
        context['active_category'] = active_category

    except ObjectDoesNotExist:
        pass
    
    context.update({"courses": courses, "categories": categories})

    return render(request, 'main.html', context)


def course_detail(request, course_id): 

    course = get_object_or_404(Course, id=course_id)

    return render(request, 'course/detail.html', {"course": course})
