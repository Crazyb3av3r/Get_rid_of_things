# Generated by Django 3.2.16 on 2022-10-29 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_thing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'fundacja'), (2, 'organizacja pozarządowa'), (3, 'zbiórka lokalna')], default=1)),
                ('categories', models.ManyToManyField(related_name='category', to='register_thing.Category')),
            ],
        ),
    ]
