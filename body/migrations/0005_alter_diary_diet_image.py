# Generated by Django 3.2.5 on 2021-11-20 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0004_diary_diet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary_diet',
            name='image',
            field=models.ImageField(blank=True, upload_to='D:\\python練習\\大二下暑假課程\\PuYuan\x08ody_%Y-%m-%d_%H:%M:%S'),
        ),
    ]