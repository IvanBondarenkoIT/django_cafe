from django.shortcuts import render
from main_page.models import UserReservation
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def reservations(request):
    messages = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reservations.html', context={'reservations': messages})
