from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Product
# Create your views here.


class IndexView(ListView):
    paginate_by = 9
    template_name = "index/index.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        qs = Product.objects.all().prefetch_related("categories")
        if query:
            qs = qs.search(query)
        return qs
