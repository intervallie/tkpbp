# Generated by Django 3.2.7 on 2021-11-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='Saran',
            field=models.TextField(max_length=200),
        ),
    ]
