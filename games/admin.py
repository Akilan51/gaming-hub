from django.contrib import admin
from .models import Category, Game, Review


admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Review)