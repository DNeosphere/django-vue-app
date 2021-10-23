# Generated by Django 3.2.4 on 2021-10-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMC_app', '0003_alter_imc_height'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('owner_name', models.CharField(max_length=50)),
                ('is_vaccinated', models.BooleanField()),
            ],
        ),
    ]
