from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brasil'),
    ('CAN', 'Canadá'),
    ('GBR', 'Reino Unido'),
    ('FRA', 'França'),
    ('GER', 'Alemanha'),
    ('ITA', 'Itália'),
    ('JPN', 'Japão'),
    ('CHN', 'China'),
    ('IND', 'Índia'),
    ('AUS', 'Austrália'),
    ('RUS', 'Rússia'),
    ('ESP', 'Espanha'),
    ('MEX', 'México'),
    ('ARG', 'Argentina'),
    ('ZAF', 'África do Sul'),
    ('NGA', 'Nigéria'),
    ('KEN', 'Quênia'),
    ('SAU', 'Arábia Saudita'),
    ('KOR', 'Coreia do Sul'),
    ('IDN', 'Indonésia'),
    ('TUR', 'Turquia'),
    ('SWE', 'Suécia'),
    ('NOR', 'Noruega'),
    ('NLD', 'Países Baixos'),
    ('BEL', 'Bélgica'),
    ('AUT', 'Áustria'),
    ('NZL', 'Nova Zelândia'),
    ('SUI', 'Suíça'),
    ('POR', 'Portugal'),
    ('POL', 'Polônia'),
    ('IRN', 'Irã'),
    ('IRQ', 'Iraque'),
    ('SYR', 'Síria'),
    ('EGY', 'Egito'),
)


class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100, 
        choices=NATIONALITY_CHOICES, 
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.name
