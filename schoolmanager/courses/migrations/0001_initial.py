# Generated by Django 5.1.2 on 2024-10-26 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('matematica', 'Matemática'), ('portugues', 'Português'), ('historia', 'História'), ('geografia', 'Geografia'), ('ciencias', 'Ciências'), ('ingles', 'Inglês'), ('ed_fisica', 'Educação Física'), ('artes', 'Artes'), ('literatura', 'Literatura'), ('quimica', 'Química'), ('fisica', 'Física'), ('biologia', 'Biologia')], max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
