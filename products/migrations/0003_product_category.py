# Generated by Django 5.0.7 on 2024-07-25 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('products', '0002_alter_product_video_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='category.category'),
        ),
    ]
