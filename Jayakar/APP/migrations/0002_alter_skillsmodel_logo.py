# Generated by Django 5.0.4 on 2024-05-05 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillsmodel',
            name='logo',
            field=models.ImageField(height_field=100, upload_to='skilllogos', width_field=100),
        ),
    ]
