from rest_framework import serializers
from .models import *
from .models import Country
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'director_name', 'age']


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'director_name', 'age', 'bio', 'director_image']


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'actor_name', ]


class ActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'actor_name', 'age', 'bio', 'actor_image']


class JanreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janre
        fields = ['id', 'janre_name']


class JanreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janre
        fields = ['id', 'janre_name', 'movie_name']


class MoviePhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePhotos
        fields = ['movie', 'image']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video', 'movie']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie', 'movie_moments']


class RatingSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField('%d-%m-%-Y %H:%M')

    class Meta:
        model = Rating
        fields = ['user', 'movie', 'status', 'parent_review', 'text', 'created_date']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = ['id', 'movie_name', ]


class HistoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['viewed_at']


class HistoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'movie', 'viewed_at']


class MovieListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'janre', 'year', 'average_rating',
                  'movie_image', 'status']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class MovieDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True, many=True)
    director = DirectorListSerializer(read_only=True, many=True)
    actor = ActorListSerializer(read_only=True, many=True)
    janre = JanreListSerializer(read_only=True, many=True)
    movie_rating = RatingSerializer(read_only=True, many=True)
    movie_language = MovieLanguagesSerializer(read_only=True, many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'country', 'director', 'actor',
                  'janre', 'types',
                  'movie_time', 'description', 'movie_trailer', 'movie_image',
                  'movie_language',
                  'status', 'movie_rating', 'average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()



