# Generated by Django 2.2.5 on 2019-09-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190913_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='name',
            field=models.CharField(help_text='A name for the map.', max_length=50, null=True),
        ),
    ]