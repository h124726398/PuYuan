# Generated by Django 3.2.5 on 2021-11-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_userprofile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userset',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='userset',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True),
        ),
    ]
