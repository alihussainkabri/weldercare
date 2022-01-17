# Generated by Django 4.0.1 on 2022-01-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welderapp', '0003_alter_new_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
