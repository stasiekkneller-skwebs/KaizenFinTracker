from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Category

User = get_user_model()

DEFAULT_CATEGORIES = [
    {"name": "Jedzenie",     "color": "#E63946"},
    {"name": "Transport",    "color": "#457B9D"},
    {"name": "Mieszkanie",   "color": "#1D3557"},
    {"name": "Rachunki",     "color": "#F4A261"},
    {"name": "Rozrywka",     "color": "#9D4EDD"},
    {"name": "Zdrowie",      "color": "#2A9D8F"},
    {"name": "Odzież",       "color": "#E76F51"},
    {"name": "Edukacja",     "color": "#264653"},
    {"name": "Oszczędności", "color": "#588157"},
    {"name": "Inne",         "color": "#6C757D"},
]

@receiver(post_save, sender=User)
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        Category.objects.bulk_create([
            Category(user=instance, name=item["name"], color=item["color"])
            for item in DEFAULT_CATEGORIES
        ])