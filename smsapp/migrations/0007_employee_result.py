# Generated by Django 3.1.5 on 2021-05-04 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0006_apidemo_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='result',
            field=models.FileField(default=1, upload_to='Results/'),
            preserve_default=False,
        ),
    ]
