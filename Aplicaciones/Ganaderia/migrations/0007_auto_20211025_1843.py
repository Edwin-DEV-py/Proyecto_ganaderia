# Generated by Django 3.1.7 on 2021-10-25 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ganaderia', '0006_auto_20211025_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
