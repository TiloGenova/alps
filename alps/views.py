from django.shortcuts import render, get_object_or_404
from .models import Activity, Contact

# Create your views here.
def home(request):
    contactall = get_object_or_404(Contact, pk=1)
    activities = Activity.objects.all()
    return render(request, 'alps/home.html', {'contactall': contactall, 'activities':activities})


def base(request):
    contactallbase = get_object_or_404(Contact, pk=1)
    return render(request, 'alps/base.html', {'contactallbase': contactallbase})


def sports(request):
    return render(request, 'alps/sports.html',)



