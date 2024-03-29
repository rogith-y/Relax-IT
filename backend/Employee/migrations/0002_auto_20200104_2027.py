# Generated by Django 3.0.2 on 2020-01-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.AlterField(
            model_name='employee',
            name='angry',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='disgusted',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='happy',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='neutral',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sad',
            field=models.IntegerField(),
        ),
    ]
