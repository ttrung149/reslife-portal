# Generated by Django 2.2.1 on 2019-05-30 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('residencies', '0001_initial'),
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='checked_out_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checked_out_by', to='staffs.Staff'),
        ),
        migrations.AddField(
            model_name='resident',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residencies.Room'),
        ),
        migrations.AddField(
            model_name='resident',
            name='under_RA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='under_RA', to='staffs.Staff'),
        ),
    ]