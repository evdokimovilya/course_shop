from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    actions = ["set_complete"]

    @admin.action(description="Set order complete")
    def set_complete(self, request, queryset):
        for order in queryset:
            order.set_complete()