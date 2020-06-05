# Generated by Django 2.2.1 on 2019-05-31 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190531_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='category', on_delete=django.db.models.deletion.CASCADE, to='shop.Category'),
        ),
    ]