# Generated by Django 3.2 on 2021-08-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='officeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_size', models.IntegerField()),
                ('office_type', models.CharField(choices=[('cm', 'Commercial'), ('in', 'Industrial'), ('rs', 'Residential')], max_length=2)),
                ('present_fire_extinguisher_number', models.IntegerField(default=0)),
                ('present_smoke_detector_number', models.IntegerField(default=0)),
            ],
        ),
    ]
