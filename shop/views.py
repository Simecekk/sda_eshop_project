from django.http import HttpResponse
from django.utils import timezone


def hello_world_view(request):
    name = request.GET.get("name")
    return HttpResponse(f"Hello world {name}")
