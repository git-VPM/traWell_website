# Generated by Django 4.0.5 on 2022-06-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='pic')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
