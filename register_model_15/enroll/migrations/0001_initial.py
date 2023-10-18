# Generated by Django 4.2.4 on 2023-08-30 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.IntegerField()),
                ('stu_name', models.CharField(max_length=70)),
                ('stu_dept', models.CharField(max_length=70)),
                ('stu_email', models.EmailField(max_length=70)),
                ('stu_pass', models.CharField(max_length=70)),
            ],
        ),
    ]
