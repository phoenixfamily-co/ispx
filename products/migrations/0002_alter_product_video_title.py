# Generated by Django 5.0.7 on 2024-07-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]