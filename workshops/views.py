from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required  # <--- 1. Importa esto
from .models import Workshop

# Vista pública (cualquiera puede entrar)
def workshop_list(request):
    workshops = Workshop.objects.all()
    context = {
        "workshops": workshops
    }
    return render(request, 'workshop/list.html', context)

# Vista protegida (pide iniciar sesión)
@login_required  # <--- 2. Agrégalo aquí encima
def workshops_details(request, id):
    workshop = get_object_or_404(Workshop, id=id)
    context = {
        "workshop": workshop
    }
    return render(request, "workshop/details.html", context)