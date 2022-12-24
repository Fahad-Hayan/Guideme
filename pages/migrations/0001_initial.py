# Generated by Django 3.2.9 on 2022-12-22 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Country Name')),
                ('image', models.ImageField(default='images/default/defaultImage.jpg', upload_to='images/%y/%m/%d', verbose_name='Photo')),
                ('activeState', models.BooleanField(default=True, verbose_name='Active State')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='City Name')),
                ('caption', models.TextField(blank=True, null=True, verbose_name='Caption')),
                ('image', models.ImageField(default='images/default/defaultImage.jpg', upload_to='images/%y/%m/%d', verbose_name='Image')),
                ('exchangeRate', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Exchage Rate')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Rating')),
                ('activeState', models.BooleanField(default=True, verbose_name='Active State')),
                ('catigory', models.CharField(choices=[('not specified', 'not specified'), ('Leisure', 'Leisure'), ('Archaeological', 'Archaeological'), ('Religious', 'Religious')], default=('not specified', 'not specified'), max_length=20)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.country')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'ordering': ['name'],
            },
        ),
    ]