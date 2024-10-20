# Generated by Django 5.1.2 on 2024-10-13 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_details_relationship_details_tagline"),
    ]

    operations = [
        migrations.AddField(
            model_name="details",
            name="facebook",
            field=models.URLField(default="-"),
        ),
        migrations.AddField(
            model_name="details",
            name="github",
            field=models.URLField(default="-"),
        ),
        migrations.AddField(
            model_name="details",
            name="instagram",
            field=models.URLField(default="-"),
        ),
        migrations.AddField(
            model_name="details",
            name="twitter",
            field=models.URLField(default="-"),
        ),
        migrations.AddField(
            model_name="details",
            name="website",
            field=models.URLField(default="-"),
        ),
    ]
