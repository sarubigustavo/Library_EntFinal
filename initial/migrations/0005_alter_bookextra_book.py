# Generated by Django 4.2.2 on 2023-07-15 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0004_bookextra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookextra',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='initial.book'),
        ),
    ]