# Generated by Django 2.1.4 on 2018-12-15 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_planeta_qtde_planeta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planeta',
            old_name='qtde_planeta',
            new_name='qtde_planetas',
        ),
    ]
