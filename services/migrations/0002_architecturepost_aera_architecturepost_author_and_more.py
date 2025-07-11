# Generated by Django 4.2.20 on 2025-07-12 08:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="architecturepost",
            name="aera",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="architecturepost",
            name="author",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="architecturepost",
            name="category",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="architecturepost",
            name="comments_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="architecturepost",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="architecturepost",
            name="is_published",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="architecturepost",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="architecturepost",
            name="tags",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="architecturepost",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
