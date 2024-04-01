from django.db import models

class Rubrika(models.Model):
    title = models.CharField (max_length = 120, blank=False)

    def __str__(self):
        return self.title
    
class Hashtag(models.Model):
    title = models.CharField(max_length = 120, blank=False)

    def __str__(self):
        return self.title
    
class Article(models.Model):
    rubNum_id = models.ForeignKey(Rubrika, on_delete=models.CASCADE)
    title = models.CharField(max_length = 120, blank=False)
    keywords = models.TextField(blank=False)
    annotation = models.TextField(blank=False)
    hashtags = models.ManyToManyField('Hashtag')

    def __str__(self):
        return self.title