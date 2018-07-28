from rest_framework import serializers
from news.models import NewsPost


class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        # fields = '__all__'
        fields = ('title', 'photo_url', 'para1', 'para2', 'para3', 'para4')
