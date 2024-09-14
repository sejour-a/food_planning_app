# Generated by Django 5.1.1 on 2024-09-14 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('section', models.CharField(choices=[('M', 'Meats'), ('V', 'Veggies'), ('D', 'Dairy & Eggs'), ('B', 'Breads'), ('O', 'Others')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now=True)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('items', models.ManyToManyField(blank=True, to='groceries.item')),
            ],
        ),
    ]
