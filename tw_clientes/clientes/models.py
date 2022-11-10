from django.db import models

# Create your models here.

class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    nome = models.CharField(max_length=100, null=False, blank=False)  #CharFild= equivalente ao varchar do mysql, não vai aceitar nulo e nem que o nome esteja em branco
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)  #já faz a validação se é um e-mail válido ou não. Se tem @ , dominio...
    profissao = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)  #vai armazenar apenas F, M ou N na DB

    # esse metodo faz com que retorne o nome e não e número que está associado a ele
    def __str__(self):
        return self.nome
