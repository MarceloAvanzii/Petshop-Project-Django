# Generated by Django 4.1 on 2022-09-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_remove_userlogin_data_nascimento_userlogin_idade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlogin',
            name='idade',
        ),
        migrations.AddField(
            model_name='userlogin',
            name='data_nascimento',
            field=models.DateField(default=None, verbose_name='Data de Nascimento'),
            preserve_default=False,
        ),
    ]
