from django.shortcuts import render, redirect
from .models import DishCategory, Dish, About, WhyUs, Events, Gallery
from .forms import UserReservationForm
import random

QTY_PHOTOS_IN_GALLERY = 8


# Create your views here.
def main_page(request):
    if request.method == 'POST':
        form_reserve = UserReservationForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')

    about_us = About.objects.all()
    why_us = WhyUs.objects.filter(is_visible=True)
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    events = Events.objects.filter(is_visible=True)
    gallery_photos = list(Gallery.objects.filter(is_visible=True))
    gallery_photos = random.sample(gallery_photos, QTY_PHOTOS_IN_GALLERY)
    form_reserve = UserReservationForm()

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'about_us': about_us[0],
        'why_us': why_us,
        'specials': special_dishes,
        'events': events,
        'gallery_photos': gallery_photos,
        'form_reserve': form_reserve,

    })

