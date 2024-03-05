from django.shortcuts import render
# from django.db.models import Q
from ice_cream.models import IceCream


def index(request):
    return render(request, 'homepage/index.html', {
        'ice_cream_list': IceCream.objects.values(
            'id', 'title', 'price', 'description'
        ).filter(
            # Проверяем, что
            is_published=True,  # Сорт разрешён к публикации;
            is_on_main=True,  # Сорт разрешён к публикации на главной странице;
            category__is_published=True  # Категория разрешена к публикации.
        )
        # .filter(
        #     Q(is_published=True)
        #     & (Q(is_on_main=True) | Q(title__contains='пломбир')))
        # .filter(is_on_main=True),
    })
