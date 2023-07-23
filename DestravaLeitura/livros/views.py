from django.shortcuts import render
from .models import LivroInfo

# Create your views here.
def livros(request):
    qs = LivroInfo.objects.order_by("nome")
    name_query = request.GET.get("bookname")

    if name_query != "" and name_query is not None:
        qs = qs.filter(nome__icontains = name_query)

    return render(request, "livros/livros.html", {"livros": qs})
