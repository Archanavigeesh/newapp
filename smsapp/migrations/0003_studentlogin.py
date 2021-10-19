# Generated by Django 3.1.5 on 2021-03-08 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0002_auto_20210308_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('std_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsapp.studentreg')),
            ],
        ),
    ]