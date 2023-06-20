# Generated by Django 4.2.1 on 2023-06-20 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeriedb', '0004_obrazy_fotka_vystava_fotka'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vystava',
            name='fotka',
        ),
        migrations.AddField(
            model_name='autori',
            name='fotka',
            field=models.ImageField(blank=True, help_text='Přidejte fotku', null=True, upload_to='vystavy', verbose_name='Fotka'),
        ),
    ]
