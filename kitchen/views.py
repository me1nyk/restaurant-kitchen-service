from django.shortcuts import render

from kitchen.models import DishType, Dish, Cook


def index(request):
    num_types = DishType.objects.count()
    num_dish = Dish.objects.count()
    num_cooks = Cook.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_types": num_types,
        "num_dish": num_dish,
        "num_cooks": num_cooks,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)
