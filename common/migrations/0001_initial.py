# Generated by Django 2.0 on 2020-06-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('planet_state', models.TextField()),
                ('planet_pic', models.ImageField(upload_to='shy_img/planet_img')),
            ],
        ),
    ]
