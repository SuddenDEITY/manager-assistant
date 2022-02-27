# Generated by Django 4.0.2 on 2022-02-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0006_client'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AddField(
            model_name='answer',
            name='type',
            field=models.CharField(choices=[('withdata', 'Логический'), ('withoutdata', 'Справочный')], default='withoutdata', max_length=20),
        ),
    ]
