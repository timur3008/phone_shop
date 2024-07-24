# Generated by Django 5.0.3 on 2024-06-11 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('name_brand', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_phone', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount', models.FloatField()),
                ('memory', models.SmallIntegerField()),
                ('color', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones_app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones_app.phone')),
            ],
        ),
    ]