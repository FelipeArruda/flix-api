from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor
from django.db.models import Avg


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
    )
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True
    )
    resume = serializers.CharField()


class MovieModelSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        """
        Usar smp get_ para o django entender que é um campo calculado
        """
        # reviews = obj.reviews.all()
        # if reviews:
        #     sum_reviews=0
        #     for review in reviews:
        #         sum_reviews += review.stars

        #     reviews_count = reviews.count()

        #     return round(sum_reviews / reviews_count, 1)

        # return reviews

        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                'A data não pode ser menor que 1990')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                'O tamanho do campo não pode ser maior que 200 caracteres')
        return value
