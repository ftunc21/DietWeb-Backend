# Generated by Django 5.0.5 on 2024-06-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('time', models.PositiveIntegerField()),
                ('difficulty', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipes/')),
            ],
        ),
    ]