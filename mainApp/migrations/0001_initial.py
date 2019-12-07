# Generated by Django 2.2.7 on 2019-12-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('mpx', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='camera')),
                ('memory', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Earphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('mpx', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='Earphone')),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generation', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=120)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('diagonal', models.FloatField()),
                ('price', models.IntegerField()),
                ('processor', models.CharField(choices=[('amd Raedon', 'AMD Raedon'), ('intel', 'Intel')], max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='laptop')),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('diagonal', models.FloatField()),
                ('price', models.IntegerField()),
                ('camera', models.IntegerField()),
                ('processor', models.CharField(choices=[('mediatek', 'Mediatek'), ('snapdragon', 'Snapdragon')], max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Smartphone')),
            ],
        ),
    ]
