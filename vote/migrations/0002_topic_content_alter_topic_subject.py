# Generated by Django 4.1.5 on 2023-01-31 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
