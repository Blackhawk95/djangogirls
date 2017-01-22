from django.db import models
from django.utils import timezone


class Post(models.Model):
    # TOPIC =(('Env','Environment'),
    #         ('Tech','Technology'),
    #         ('Auto','Automotive'),
    #         ('Otr','Others'),
    # )
    author = models.ForeignKey('auth.User', default = "abhijith")
    title = models.CharField(max_length=200, default = "Enter the title")
    # topic = models.CharField(max_length=1, choices=TOPIC)
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
