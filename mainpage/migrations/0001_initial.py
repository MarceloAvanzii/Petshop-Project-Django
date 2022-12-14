# Generated by Django 4.1 on 2022-09-30 14:23

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome_completo', models.CharField(max_length=256, verbose_name='Nome Completo')),
                ('emailfield', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('celular', models.CharField(max_length=256, verbose_name='Celular')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('idade', models.IntegerField(verbose_name='Idade')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
