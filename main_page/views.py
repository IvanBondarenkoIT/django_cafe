from django.shortcuts import render
from .models import DishCategory, Dish, About, WhyUs, Events
from django.http import HttpResponse


# Create your views here.
def main_page(request):
    about_us = About.objects.all()
    why_us = WhyUs.objects.filter(is_visible=True)
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    events = Events.objects.filter(is_visible=True)
    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'about_us': about_us[0],
        'why_us': why_us,
        'specials': special_dishes,
        'events': events,
    })
    # return HttpResponse('\n'.join(map(str, categories)) + '\n'.join(map(str, dishes)))
