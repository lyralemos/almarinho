# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed

from models import Entry

class LatestEntriesFeed(Feed):
    title = "Alexandre Marinho"
    link = "/sitenews/"
    description = "Últimos posts de almarinho.com.br"
    description_template = "core/feed.html"

    def items(self):
        return Entry.objects.order_by('-data_publicacao')[:5]

    def item_title(self, item):
        return item.titulo