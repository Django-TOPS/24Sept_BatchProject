# Generated by Django 3.1.4 on 2020-12-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('sub', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=12)),
            ],
        ),
    ]
