# Generated by Django 2.2.1 on 2019-05-30 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residencies', '0005_auto_20190530_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='student_email',
            field=models.EmailField(max_length=254),
        ),
    ]