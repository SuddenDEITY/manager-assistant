# Generated by Django 4.0.2 on 2022-02-26 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0005_remove_question_answer_answer_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
            ],
        ),
    ]
