from django.db import models
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery
import operator
import functools
from django.conf import settings


class ProductQuerySet(models.QuerySet):
    def search(self, query):
        if settings.IS_DB_POSTGRES:
            search_q = [SearchQuery(i) for i in query.split()]
            search_q = functools.reduce(operator.or_, search_q)
            return self.annotate(
                search=SearchVector('title', 'description', 'source', 'colour'),
            ).filter(search=search_q)

        #### for sqlite
        regex = r"\b({})\b".format("|".join(query.split()))
        return self.filter(
            Q(title__iregex=regex)|\
            Q(description__iregex=regex)|\
            Q(source__iregex=regex)|\
            Q(colour__iregex=regex)
        )


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
