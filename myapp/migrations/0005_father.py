# Generated by Django 3.2.6 on 2021-08-28 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210828_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Father',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True, unique=True)),
                ('age', models.BigIntegerField(default=12, null=True)),
            ],
        ),
    ]