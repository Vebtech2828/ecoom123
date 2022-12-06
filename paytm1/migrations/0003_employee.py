# Generated by Django 4.1.3 on 2022-11-29 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paytm1', '0002_jobdata_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=64)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=64)),
            ],
        ),
    ]
