# Generated by Django 2.2.14 on 2020-12-12 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
