# Generated by Django 3.2.15 on 2023-01-18 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "registration",
            "0009_rename_custom_choice_application_specific_dietary_requirement",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="dietary_restrictions",
            field=models.CharField(
                choices=[
                    (None, ""),
                    ("none", "None"),
                    ("halal", "Halal"),
                    ("vegetarian", "Vegetarian"),
                    ("gluten-Free", "Gluten-free"),
                    ("other but specify", "Other but Specify"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="what_hackathon_experience",
            field=models.TextField(
                help_text="If you’ve been to a hackathon, briefly tell us your experience. If not, describe what you expect to see and experience.",
                max_length=1000,
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="what_technical_experience",
            field=models.TextField(
                help_text="What is your technical experience with software and hardware?",
                max_length=1000,
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="why_participate",
            field=models.TextField(
                help_text="Why do you want to participate in MakeUofT?", max_length=1000
            ),
        ),
    ]
