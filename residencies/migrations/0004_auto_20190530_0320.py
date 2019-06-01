# Generated by Django 2.2.1 on 2019-05-30 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('residencies', '0003_auto_20190530_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='student_email',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='resident',
            name='checked_out_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checked_out_by', to='staffs.Staff'),
        ),
    ]
