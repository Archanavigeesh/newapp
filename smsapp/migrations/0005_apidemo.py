# Generated by Django 3.1.5 on 2021-04-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0004_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apidemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('contact', models.IntegerField()),
                ('place', models.CharField(max_length=25)),
            ],
        ),
    ]
