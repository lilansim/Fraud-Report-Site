# Generated by Django 4.2.1 on 2023-06-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReportSystem', '0002_auto_20221129_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fraudreport',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reporthistory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]