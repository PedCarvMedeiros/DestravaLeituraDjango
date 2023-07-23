import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DestravaLeitura.settings")

import django
django.setup()

import random
from livros.models import *

from faker import Faker
fakegen = Faker()


def populate(N=10):
    for entry in range(N):

        fake_nome = fakegen.first_name()
        fake_autor = fakegen.first_name()
        fake_genero = fakegen.first_name()
        fake_xerox = fakegen.first_name()
        fake_emprestado = fakegen.first_name()


        livro = LivroInfo.objects.get_or_create(nome=fake_nome, autor=fake_autor, genero=fake_genero, xerox=fake_xerox, emprestado=fake_emprestado)[0]

if __name__ == "__main__":
    populate(20)
    print("Population completed")