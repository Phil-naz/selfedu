from django.db.models import Count

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},]

class DataMixin:
    paginate_by = 3  # count of articles, included 1 page

    def get_user_context(self, **kwargs):
        context = kwargs
#        cats = Category.objects.all()   # forming list of categories
        cats = Category.objects.annotate(Count('women'))

        user_menu = menu.copy()               # make copy
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu            # context for menu

        context['cats'] = cats                 # context for categories
#        if 'cat_selected' not in context:
#            context['cat_selected'] = 0        default value
        return context