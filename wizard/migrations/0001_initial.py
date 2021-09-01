# Generated by Django 3.2.6 on 2021-09-01 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wizard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('house', models.CharField(max_length=45)),
                ('pet', models.CharField(max_length=45)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
