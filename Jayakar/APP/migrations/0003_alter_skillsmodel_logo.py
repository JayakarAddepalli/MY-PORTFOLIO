# Generated by Django 5.0.4 on 2024-05-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_alter_skillsmodel_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillsmodel',
            name='logo',
            field=models.ImageField(upload_to='skilllogos'),
        ),
    ]
