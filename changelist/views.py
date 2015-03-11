from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from changelist.models import Petition


def list(request):
    ctx = {
        'petitions': Petition.objects.all()
    }
    return render(request, 'changelist/list.html', ctx)

def details(request, pk):
    petition = get_object_or_404(Petition, pk=pk)
    ctx = {'petition': petition}

    if 'q' in request.GET:
        ctx['signatures'] = petition.signature_set.filter(
            Q(name__icontains=request.GET['q']) | Q(city__icontains=request.GET['q']))

    return render(request, 'changelist/details.html', ctx)