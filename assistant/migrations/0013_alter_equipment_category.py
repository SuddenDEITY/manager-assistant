# Generated by Django 4.0.2 on 2022-03-04 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0012_alter_eq_characteristics_equipment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cat_equipment', to='assistant.eq_category'),
        ),
    ]