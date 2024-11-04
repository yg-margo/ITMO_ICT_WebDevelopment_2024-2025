from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.postgres import fields


class Country(models.Model):
    country_name = models.CharField(max_length=100, verbose_name='Country')

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class FoodType(models.Model):
    type = models.CharField(max_length=100, verbose_name="Food type")

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Food type"
        verbose_name_plural = "Food types"


class Tour(models.Model):
    name = models.CharField(max_length=200, verbose_name='Tour name')
    country = models.ManyToManyField(Country, verbose_name='Country')
    city = models.CharField(max_length=200, verbose_name='City')
    available_dates = fields.ArrayField(models.DateField(),
                                        verbose_name='Available dates',
                                        default=list)
    duration = models.IntegerField(verbose_name='Duration')
    tour_agency = models.CharField(max_length=100, verbose_name="Travel agency")

    food_type = models.ManyToManyField(FoodType, verbose_name="Food type")
    hotel_category = fields.ArrayField(
        models.IntegerField(validators=[MinValueValidator(1),
                                        MaxValueValidator(5)]),
        verbose_name='Hotel category', default=list)
    description = models.CharField(max_length=1000, verbose_name='Description')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'


class Tourist(AbstractUser):
    tours = models.ManyToManyField(Tour, through='TourBooking',
                                   verbose_name='Tours',
                                   related_name='tourists', blank=True)


class TourBooking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE,
                             verbose_name='Tour')
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE,
                                verbose_name='Tourist')
    selected_date = models.DateField(verbose_name='Selected date')
    selected_category = models.IntegerField(verbose_name='Hotel category',
                                            validators=[MinValueValidator(1),
                                                        MaxValueValidator(5)])
    persons_number = models.IntegerField(verbose_name='Number of adults')
    children_number = models.IntegerField(verbose_name='Number of children')
    rooms_number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Number of rooms')

    STATUSES = (
        ('W', "Ожидает подтверждения"),
        ('B', 'Забронирован'),
        ('C', 'Отказано'),
        ('D', 'Завершен')
    )
    status = models.CharField(choices=STATUSES, max_length=100,
                              verbose_name='Booking status')

    def __str__(self):
        return self.tour.name

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'


class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE,
                             verbose_name='Tour')
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE,
                                verbose_name='Tourist')
    text = models.CharField(max_length=1000, verbose_name='Review text')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)],
                                 verbose_name='Grade')
    booking = models.ForeignKey(TourBooking, on_delete=models.CASCADE,
                                verbose_name="Booking")

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
