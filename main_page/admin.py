from django.contrib import admin
from .models import DishCategory, Dish, About, WhyUs, Events


# Register your models here.
admin.site.register(Dish)
admin.site.register(DishCategory)
admin.site.register(About)
admin.site.register(WhyUs)
admin.site.register(Events)
