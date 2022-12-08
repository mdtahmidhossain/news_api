from rest_framework import serializers
from web.models import Article, Source


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    source = SourceSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
