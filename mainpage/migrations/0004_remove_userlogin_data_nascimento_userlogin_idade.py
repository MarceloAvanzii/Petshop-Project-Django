# Generated by Django 4.1 on 2022-09-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_remove_userlogin_idade_userlogin_data_nascimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlogin',
            name='data_nascimento',
        ),
        migrations.AddField(
            model_name='userlogin',
            name='idade',
            field=models.IntegerField(default=0, verbose_name='Idade'),
            preserve_default=False,
        ),
    ]
