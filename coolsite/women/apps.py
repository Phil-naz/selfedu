from django.apps import AppConfig


class WomenConfig(AppConfig):
    name = 'women'
    verbose_name = "Женщины мира" # заголовок в админке на синей плашке

class CategoryConfig(AppConfig):
    name = 'Category'
    verbose_name = "Категории" # заголовок в админке на синей плашке
