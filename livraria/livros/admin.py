from django.contrib.admin import site
from django.contrib import admin
from .models import Livro, Autores, Categoria, Editora

import adminactions.actions as actions

admin.site.register(Livro)
actions.add_to_site(site)
