from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipe(request, name):
    if name in DATA:
        servings = int(request.GET.get("servings", 1))
        recipe = {}
        for key, item in DATA[name].items():
            recipe[key] = item*servings
        print(recipe)
        context = {
            'recipe': recipe
        }
        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse('Рецепт отсутствует')
