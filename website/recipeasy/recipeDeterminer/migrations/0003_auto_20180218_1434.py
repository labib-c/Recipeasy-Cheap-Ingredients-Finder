# Generated by Django 2.0.2 on 2018-02-18 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipeDeterminer', '0002_auto_20180218_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipeDeterminer.Recipe'),
        ),
    ]
