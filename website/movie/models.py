from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField


class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18), MaxValueValidator(100)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    STATUS_CHOICES = (
        ('pro', 'Pro'),
        ('simple', 'Simple',)
    )
    status = models.CharField(max_length=35, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return f'{self.username}'


class Country(models.Model):
    country_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(default=0)
    director_image = models.ImageField(upload_to='director_images/')

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(default=0)
    actor_image = models.ImageField(upload_to='actor_images/')

    def __str__(self):
        return self.actor_name


class Janre(models.Model):
    janre_name = models.CharField(max_length=32)

    def __str__(self):
        return self.janre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=32)
    year = models.PositiveSmallIntegerField()
    country = models.ManyToManyField(Country, related_name='country_movies')
    director = models.ManyToManyField(Director, related_name='director_movies')
    actor = models.ManyToManyField(Actor, related_name='actor_movies')
    janre = models.ManyToManyField(Janre, related_name='janre_movies')
    TYPES_CHOICES = (
        ('144', '144'),
        ('360', '360'),
        ('480', '480'),
        ('720', '720'),
        ('1080', '1080'),
    )
    types = MultiSelectField(choices=TYPES_CHOICES)
    movie_time = models.DateField(auto_now=True)
    description = models.TextField()
    movie_trailer = models.FileField(max_length=50, verbose_name='Видео',)
    movie_image = models.ImageField(upload_to='movie_image/')
    MOVIE_STATUS=(
        ('pro', 'Pro'),
        ('simple', 'Simple',)
    )
    status = models.CharField(max_length=35, choices=MOVIE_STATUS, default='pro')

    def __str__(self):
        return self.movie_name

    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0


class MoviePhotos(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='movie_images/')


class MovieLanguages(models.Model):
    language = models.CharField(max_length=50)
    video = models.FileField(upload_to='movie_images/')
    movie = models.ForeignKey(Movie, related_name='movie_languages', on_delete=models.CASCADE)


class Moments(models.Model):
    movie = models.FileField(max_length=50)
    movie_moments = models.ForeignKey(Movie, related_name='moments', on_delete=models.CASCADE)


class Rating(models.Model):
    user = models.ManyToManyField(Profile)
    movie = models.ManyToManyField(Movie, related_name='ratings')
    status = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], verbose_name="Рейтинг", null=True, blank=True)
    parent = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie} - {self.status} status"


class Favorite(models.Model):
    user = models.ManyToManyField(Profile)
    created_date = models.DateTimeField(auto_now_add=True)


class FavoriteMovie(models.Model):
    cart = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='cart')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class History(models.Model):
    user = models.ForeignKey(Profile, related_name='history_user', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movie_history', on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

