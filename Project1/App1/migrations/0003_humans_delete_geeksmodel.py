# Generated by Django 4.1.2 on 2022-10-15 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App1", "0002_remove_geeksmodel_img_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Humans",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "my_field_name",
                    models.CharField(
                        help_text="Enter field documentation", max_length=20
                    ),
                ),
            ],
            options={"ordering": ["-my_field_name"],},
        ),
        migrations.DeleteModel(name="GeeksModel",),
    ]
