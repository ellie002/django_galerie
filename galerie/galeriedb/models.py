from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Vystava(models.Model):
    nazev = models.CharField(max_length=80, verbose_name="Název výstavy", help_text="Zadejte název výstavy")
    popis = models.TextField(max_length=4000, blank=True, null=True, help_text="Zadejte popis výstavy")
    mistnosti = models.ManyToManyField("Mistnosti", verbose_name="Čísla místností", help_text="Zadejte číslo místnosti")
    obrazy = models.ManyToManyField("Obrazy", verbose_name="Obrazy na výstavě", help_text="Zadejte obrazy na výstavě")

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Vystava'
        verbose_name_plural = 'Vystavy'

    def __str__(self):
        return f'{self.nazev}'


class Obrazy(models.Model):
    
    nazev = models.CharField(max_length=80, verbose_name="Název obrazu", help_text="Zadejte název obrazu")
    popis = models.TextField(max_length=4000, blank=True, null=True, help_text="Zadejte popis obrazu")
    autor = models.ForeignKey("Autori", on_delete=models.CASCADE, verbose_name="Jméno autora", help_text="Zadejte jméno autora")
    mistnost = models.ForeignKey("Mistnosti", on_delete=models.CASCADE, verbose_name="Číslo místnosti", help_text="Zadejte číslo místnosti")

    class Meta:
        ordering =['nazev']
        verbose_name = 'Obraz'
        verbose_name_plural = 'Obrazy'

    def __str__(self):
        return f'{self.nazev}'
    

class Autori(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name="Jméno autora", help_text="Zadejte jméno autora") 
    prijmeni = models.CharField(max_length=80, verbose_name="Příjmení autora", help_text="Zadejte příjmení autora")
    rok_narozeni = models.IntegerField(verbose_name="Rok narození autora", help_text="Zadejte rok narození autora",
                                       validators=[MinValueValidator(0, message='Hodnota musí být větší nebo rovna 0.'),
                                                MaxValueValidator(2023, message='Hodnota musí být menší nebo rovna 2023.')])
    rok_umrti = models.IntegerField(verbose_name="Rok úmrtí autora", help_text="Zadejte rok úmrtí autora", 
                                    validators=[MinValueValidator(0, message='Hodnota musí být větší nebo rovna 0.'),
                                                MaxValueValidator(2023, message='Hodnota musí být menší nebo rovna 2023.')])
    
    class Meta:
        ordering =['jmeno']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autori'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'
    

class Mistnosti(models.Model):

    PODLAZI_CHOICES = (
        ('Přízemí', 'Přízemí'),
        ('1. patro', '1. patro'),
        ('2. patro', '2. patro'),
        ('Neznámé', 'Neznámé')
    )

    cislo_mistnosti = models.IntegerField(verbose_name="Číslo místnosti", help_text="Zadejte číslo místnosti")
    podlazi = models.CharField(max_length=10, choices=PODLAZI_CHOICES, default="Neznámé", verbose_name="Podlaží", help_text="Zadejte podlaží místnosti")

    class Meta:
        ordering =['cislo_mistnosti']
        verbose_name = 'Mistnost'
        verbose_name_plural = 'Mistnosti'

    def __str__(self):
        return f'{self.cislo_mistnosti}'


