# Generated by Django 4.0.1 on 2022-01-17 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welderapp', '0002_rename_news_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='color',
            field=models.CharField(choices=[('#FFFADE', 'Light Cream'), ('#E3F5FF', 'Sky Blue'), ('#FFEAEA', 'Pink'), ('#EBEAFC', 'Light Purple'), ('#FFF3E2', 'Dark Cream')], default='#FFFADE', max_length=10),
        ),
    ]