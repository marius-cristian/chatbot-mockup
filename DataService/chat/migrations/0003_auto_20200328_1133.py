# Generated by Django 2.2.11 on 2020-03-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='name',
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]