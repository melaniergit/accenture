from django.db import models
from uuid import uuid4


class Categoria(models.Model):
    id_categoria = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    categoria_text = models.CharField(max_length=50)

    def __str__(self):
        return "%s (%s)" % (self.id_categoria, self.categoria_text)


class Editora(models.Model):
    id_editora = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    editora_text = models.CharField(max_length=50)

    def __str__(self):
        return "%s (%s)" % (self.id_editora, self.editora_text)


class Autores(models.Model):
    id_autor = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    autores_text = models.CharField(max_length=50)

    def __str__(self):
        return "%s (%s)" % (self.id_autor, self.autores_text)


class Livro(models.Model):

    id_livro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros")
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros")
    autores = models.ManyToManyField(Autores, related_name="livros")

    def __str__(self):
        return "%s (%s)" % (self.titulo, self.editora,self.categoria,self.autores)










