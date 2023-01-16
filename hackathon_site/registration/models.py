from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model
import uuid

from hackathon_site import settings
from registration.validators import UploadedFileValidator

User = get_user_model()


def _generate_team_code():
    team_code = uuid.uuid4().hex[:5].upper()
    while Team.objects.filter(team_code=team_code).exists():
        team_code = uuid.uuid4().hex[:5].upper()
    return team_code


class Team(models.Model):
    team_code = models.CharField(max_length=5, default=_generate_team_code, null=False)

    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    MAX_MEMBERS = 4

    def __str__(self):
        return self.team_code


class Application(models.Model):
    GENDER_CHOICES = [
        (None, ""),
        ("male", "Male"),
        ("female", "Female"),
        ("non-binary", "Non-binary"),
        ("other", "Other"),
        ("no-answer", "Prefer not to answer"),
    ]

    ETHNICITY_CHOICES = [
        (None, ""),
        ("american-native", "American Indian or Alaskan Native"),
        ("asian-pacific-islander", "Asian / Pacific Islander"),
        ("black-african-american", "Black or African American"),
        ("hispanic", "Hispanic"),
        ("caucasian", "White / Caucasian"),
        ("other", "Multiple ethnicity / Other"),
        ("no-answer", "Prefer not to answer"),
    ]

    STUDY_LEVEL_CHOICES = [
        (None, ""),
        ("highschool", "High School"),
        ("undergraduate", "Undergraduate"),
        ("gradschool", "Graduate School"),
        ("other", "Other"),
    ]

    TSHIRT_SIZE_CHOICES = [
        (None, ""),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
    ]

    HACKATHON_NUMBER_CHOICES = [
        (None, ""),
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5 or more", "5 or more"),
    ]

    DIETARY_RESTRICTIONS_CHOICES = [
        (None, ""),
        ("halal", "Halal"),
        ("vegetarian", "Vegetarian"),
        ("gluten-Free", "Gluten-free"),
        ("other but specify", "Other but Specify"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    team = models.ForeignKey(
        Team, related_name="applications", on_delete=models.CASCADE, null=False
    )

    # User Submitted Fields
    birthday = models.DateField(null=False)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=False)
    ethnicity = models.CharField(max_length=50, choices=ETHNICITY_CHOICES, null=False)
    country = models.CharField(
        max_length=255, null=True, blank=True, help_text="Country (Optional)"
    )
    city = models.CharField(
        max_length=255, null=True, blank=True, help_text="City (Optional)"
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        validators=[
            validators.RegexValidator(
                r"^(?:\+\d{1,3})?\s?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}$",
                message="Enter a valid phone number.",
            )
        ],
    )
    tshirt_size = models.CharField(
        max_length=50, choices=TSHIRT_SIZE_CHOICES, null=False
    )
    dietary_restrictions = models.CharField(
        max_length=50, choices=DIETARY_RESTRICTIONS_CHOICES, null=False
    )
    custom_choice = models.CharField(max_length=50, blank=True)
    school = models.CharField(max_length=255, null=False)
    study_level = models.CharField(
        max_length=50, choices=STUDY_LEVEL_CHOICES, null=False
    )
    program = models.CharField(max_length=255, help_text="Program or Major", null=False)
    graduation_year = models.IntegerField(
        null=False,
        validators=[
            validators.MinValueValidator(
                2000, message="Enter a realistic graduation year."
            ),
            validators.MaxValueValidator(
                2030, message="Enter a realistic graduation year."
            ),
        ],
    )
    resume = models.FileField(
        upload_to="applications/resumes/",
        validators=[
            UploadedFileValidator(
                content_types=["application/pdf"], max_upload_size=20 * 1024 * 1024
            )
        ],
        null=False,
    )
    how_many_hackathons = models.TextField(
        null=False,
        help_text="How many hackathons have you been to?",
        choices=HACKATHON_NUMBER_CHOICES,
        max_length=100,
    )
    what_hackathon_experience = models.TextField(
        null=False,
        help_text="If you’ve been to a hackathon, briefly tell "
        "us your experience. If not, describe what you"
        " expect to see and experience. (1000 chars. "
        "max)",
        max_length=1000,
    )
    why_participate = models.TextField(
        null=False,
        help_text="Why do you want to participate in MakeUofT? (1000 chars. max)",
        max_length=1000,
    )
    what_technical_experience = models.TextField(
        null=False,
        help_text="What is your technical experience with software and hardware? (1000 chars. max)",
        max_length=1000,
    )
    referral_source = models.TextField(
        null=False,
        help_text=f"How did you hear about {settings.HACKATHON_NAME}?",
        max_length=1000,
    )
    resume_sharing = models.BooleanField(
        help_text="I consent to IEEE UofT sharing my resume with event sponsors. (Optional)",
        blank=True,
        null=False,
        default=False,
    )

    rsvp = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def save(self, *args, **kwargs):
        if (
            self.dietary_restrictions == "other but specify"
            or self.dietary_restrictions == "Other but Specify"
        ):
            self.dietary_restrictions = self.custom_choice
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
