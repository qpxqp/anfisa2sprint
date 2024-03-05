from django.shortcuts import render, get_object_or_404
from .models import IceCream


def ice_cream_detail(request, pk):
    # template = 'ice_cream/detail.html'
    # context = {}
    return render(request, 'ice_cream/detail.html', {
        'ice_cream': get_object_or_404(
            IceCream.objects.all()
            .filter(is_published=True, category__is_published=True)
            .select_related('wrapper')
            .select_related('category')
            .prefetch_related('toppings'),
            pk=pk
        )
    })


def ice_cream_list(request):
    return render(request, 'ice_cream/list.html', {
        'ice_cream_list': IceCream.objects.all()
        .filter(is_published=True, category__is_published=True)
        .select_related('wrapper')
        .select_related('category')
        .order_by('title')
    })
