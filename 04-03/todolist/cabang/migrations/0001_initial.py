# Generated by Django 2.2 on 2020-09-09 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('jenisobat', models.TextField(default='')),
                ('quantity', models.TextField(default='')),
            ],
        ),
    ]
