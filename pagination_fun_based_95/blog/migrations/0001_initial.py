# Generated by Django 4.2.4 on 2023-10-02 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post_body', models.TextField(max_length=500)),
                ('publish_date', models.DateTimeField()),
            ],
        ),
    ]
