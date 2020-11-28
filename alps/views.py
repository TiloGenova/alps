from django.shortcuts import render, get_object_or_404
from .models import Activity, Contact

# Create your views here.


def home(request):
    contactall = get_object_or_404(Contact, pk=1)
    activities = Activity.objects.all()
    sport_activities = Activity.objects.filter(category='sport')[:4]
    enos = Activity.objects.filter(category='after ski')[:2]
    places = Activity.objects.filter(category='luoghi')[:2]

    return render(request, 'alps/home.html', {'contactall': contactall, 'activities': activities,
                                              'sport_activities': sport_activities,
                                              'enos': enos, 'places': places})


def base(request):
    contactallbase = get_object_or_404(Contact, pk=1)
    return render(request, 'alps/base.html', {'contactallbase': contactallbase})


def contatti(request):
    return render(request, 'alps/contatti.html',)


def sports(request):
    contactall = get_object_or_404(Contact, pk=1)
    sport_activities = Activity.objects.filter(category='sport')
    # sport_activities = Activity.objects.get(category='sport')   -- GET only for one object
    enos = Activity.objects.filter(category='after ski')[:2]
    places = Activity.objects.filter(category='luoghi')[:2]
    return render(request, 'alps/sports.html', {'contactall': contactall, 'sport_activities': sport_activities,
                                                'enos': enos, 'places': places})


def luoghi(request):
    contactall = get_object_or_404(Contact, pk=1)
    sport_activities = Activity.objects.filter(category='sport')[:2]
    enos = Activity.objects.filter(category='after ski')[:2]
    places = Activity.objects.filter(category='luoghi')
    return render(request, 'alps/luoghi.html', {'contactall': contactall, 'sport_activities': sport_activities,
                                                'enos': enos, 'places': places})


def details(request, activity_id):
    contactall = get_object_or_404(Contact, pk=1)
    activities = Activity.objects.all()
    activity_id = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'alps/details.html', {'contactall': contactall, 'id': activity_id})
