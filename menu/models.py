from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(
        max_length=100, null=True, help_text="Use it in templatetag for displaying menu"
    )
    named_url = models.CharField(
        max_length=100, blank=True, help_text="Named url from urls.py"
    )

    class Meta:
        verbose_name_plural = "menu"

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse(self.named_url) if self.named_url else "/{}/".format(self.slug)


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu, related_name="items", blank=True, null=True, on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="items",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    url = models.CharField(
        max_length=100, blank=True, help_text="Don't forget to put '/' on both sides"
    )
    named_url = models.CharField(
        max_length=255,
        verbose_name="Named URL",
        blank=True,
        help_text="Named url from urls.py",
    )

    class Meta:
        verbose_name_plural = "menu items"

    def get_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            return reverse(self.named_url)
        else:
            return "/"

    def __str__(self):
        return self.name
