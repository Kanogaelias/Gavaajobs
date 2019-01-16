# Generated by Django 2.0.7 on 2018-07-13 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(max_length=5000, verbose_name='Description')),
                ('company', models.CharField(max_length=255, verbose_name='Company')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
            ],
        ),
    ]
