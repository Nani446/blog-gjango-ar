# Generated by Django 3.2.6 on 2021-08-31 21:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_book_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=1),
        ),
    ]
