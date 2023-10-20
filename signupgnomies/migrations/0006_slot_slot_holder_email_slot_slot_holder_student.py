# Generated by Django 4.2.5 on 2023-10-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupgnomies', '0005_remove_category_fills_category_number_of_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='slot_holder_email',
            field=models.EmailField(default='gnomie@example.com', max_length=255),
        ),
        migrations.AddField(
            model_name='slot',
            name='slot_holder_student',
            field=models.CharField(default='gnome', max_length=52),
        ),
    ]