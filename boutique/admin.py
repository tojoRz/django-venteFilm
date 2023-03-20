from django.contrib import admin

from .models import Reservation, Contact, Film, Genre

# Register your models here.


class ReservationInline(admin.TabularInline):
    readonly_fields = ["create_at", "film", 'contacted']
    model = Reservation
    fieldsets = [
        (None, {'fields': ['film','contacted']})
    ]
    extra = 0 
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"

    def has_add_permission(self, request):
        return False

class FilmGenreInline(admin.TabularInline):
    model = Film.genres.through
    extra = 1
    verbose_name = "Film"
    verbose_name_plural = "Films"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = []

    def has_add_permission(self, request):
        return False

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    inlines = [FilmGenreInline,]

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'titre']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    readonly_fields = ["create_at", "contact", "film"]
    list_filter = ['create_at', 'contacted']

    def has_add_permission(self, request):
        return False

    