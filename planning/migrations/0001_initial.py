# Generated by Django 5.1.1 on 2024-09-14 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groceries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday_date', models.DateField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, max_length=1024)),
                ('recipe', models.TextField(blank=True, max_length=4096)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('recipe_url', models.URLField(blank=True, null=True)),
                ('ingredients', models.ManyToManyField(blank=True, to='groceries.item')),
            ],
            options={
                'verbose_name_plural': 'dishes',
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('dinner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dinner_on_days_set', to='planning.dish')),
                ('lunch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lunch_on_days_set', to='planning.dish')),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planning.week')),
            ],
        ),
    ]
