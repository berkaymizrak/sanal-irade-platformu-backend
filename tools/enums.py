from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class SocialMediaIcons(TextChoices):
    FACEBOOK = "facebook", _("Facebook")
    TWITTER = "twitter", _("Twitter")
    GITHUB = "github", _("Github")
    INSTAGRAM = "instagram", _("Instagram")
    TELEGRAM = "telegram", _("Telegram")
