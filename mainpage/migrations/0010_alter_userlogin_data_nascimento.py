# Generated by Django 4.1 on 2022-09-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_remove_userlogin_datanascimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='data_nascimento',
            field=models.IntegerField(null=True, verbose_name='Data de Nascimento'),
        ),
    ]