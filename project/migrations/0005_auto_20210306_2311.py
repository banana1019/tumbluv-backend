# Generated by Django 3.1.7 on 2021-03-06 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210306_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.community'),
        ),
    ]
