# Generated by Django 2.2.7 on 2019-12-06 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20191206_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='processor',
            field=models.CharField(choices=[('amd Raedon', 'AMD Raedon'), ('intel', 'Intel')], max_length=100),
        ),
    ]