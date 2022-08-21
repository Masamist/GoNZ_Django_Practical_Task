from django.contrib import admin

from .models import Tour


class TourAdmin(admin.ModelAdmin):
    model = Tour

    list_display = [
        "tour_name",
        "city_name",
        "agent",
        "date",
    ]


# Register your models here.
admin.site.register(Tour, TourAdmin)
