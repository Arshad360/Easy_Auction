# Generated by Django 4.0.3 on 2022-04-09 07:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0007_listing_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='auction_end_date_time',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='None/NIA.png', upload_to=''),
        ),
    ]
