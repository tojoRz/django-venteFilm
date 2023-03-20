from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError


from .models import Genre, Contact, Film, Reservation
from .forms import ContactForm, ParagraphErrorList


# Create your views here.
def index(request):
    film = Film.objects.filter(disponible=True).order_by('-create_at')[:12]
    formatted_film = ["<li>{}</li>".format(films(films.titre) for films in film)]
    context = {
        'film': film
    } 
    return render(request, 'boutique/index.html', context)


def listes(request):
    film_list = Film.objects.filter(disponible=True)
    paginator = Paginator(film_list, 6)
    page = request.GET.get('page')
    try:
        film = paginator.page(page)
    except PageNotAnInteger:
        film = paginator.page(1)
    except EmptyPage:
        film = paginator.page(paginator.num_pages)
    context = {
        'film': film,
        'paginate': True
    }
    return render(request, 'boutique/listing.html', context)


def detail(request, films_id):
    films = Film.objects.get(pk=films_id) 
    genres_name = " ".join([genre.name for genre in films.genres.all()])
    context = {
        'films_titre': films.titre,
        'films_name': genres_name,
        'films_id': films.id,
        'thumbnail': films.photo,    
    }
    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():

            email = form.cleaned_data['email']
            nom = form.cleaned_data['nom']

            try:
                with transaction.atomic():
                    contact = Contact.objects.filter(email=email)
                    if not contact.exists():
                        contact = Contact.objects.create(
                            email=email,
                            nom=nom
                        )
                    else:
                        contact = contact.first()
                    films = Film.objects.get(id=films_id)
                    reservation = Reservation.objects.create(
                        contact=contact,
                        film=films
                    )
                    films.disponible = False
                    films.save()
                    context = {
                        'films_titre': films.titre
                    }
                    return render(request, 'boutique/merci.html', context)
            except IntegrityError:     
                form.errors['internal'] = "Une error interne est apparue. Merci de recommencer à nouveau."   

    else:
        form = ContactForm()
    
    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'boutique/detail.html', context)


def search(request):
    query = request.GET.get('query')
    if not query:
        film = Film.objects.all()
    else:
        film = Film.objects.filter(titre__contains = query)

        if not film.exists():
            film = Film.objects.filter(genres__name__contains=query)

    titre = "Résultat pour la requête %s"%query
    context = {
        'film': film,
        'titre': titre   
        }
    return render(request, 'boutique/search.html', context)