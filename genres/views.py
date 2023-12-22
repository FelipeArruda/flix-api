import json
from django.http import JsonResponse
from genres.models import Genre
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError, ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import get_object_or_404


@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = []
        for genre in genres:
            data.append(
                {'id': genre.id, 'name': genre.name}
            )
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name', '')

        try:
            existing_genre = Genre.objects.get(name__iexact=name)
            return JsonResponse(
                {'error': f'Genre with name "{name}" already exists.'},
                status=400
            )
        except Genre.DoesNotExist:
            try:
                new_genre = Genre(name=name)
                new_genre.full_clean()  # Validate uniqueness
                new_genre.save()
                return JsonResponse({
                    'id': new_genre.id,
                    'name': new_genre.name
                }, status=201)
            except ValidationError as e:
                return JsonResponse({'error': e.message}, status=400)
        except MultipleObjectsReturned:
            return JsonResponse(
                {'error': f'Multiple genres with name "{name}" found. Database is corrupted.'},
                status=500
            )


@csrf_exempt
def genre_detail_view(request, pk):
    try:
        genre = get_object_or_404(Genre, pk=pk)
        if request.method == 'GET':
            data = {'id': genre.id, 'name': genre.name}
            return JsonResponse(data)
        elif request.method == 'PUT':
            data = json.loads(request.body.decode('utf-8'))
            genre.name = data['name']
            genre.full_clean()  # Validate uniqueness
            genre.save()
            return JsonResponse(
                {
                    'id': genre.id,
                    'name': genre.name
                }, status=201)
        elif request.method == 'DELETE':
            genre.delete()
            return JsonResponse(
                {
                    'message': f'Genre with name "{genre.name}" deleted.',
                }, status=204)
    except ValidationError as e:
        return JsonResponse({'error': e.message}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
