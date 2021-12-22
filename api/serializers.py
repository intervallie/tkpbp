from rest_framework import serializers
from article.models import Article
from donation.models import Donasi
class ArtikelPhotoSerializer(serializers.ModelSerializer):
    # photo = serializers.ImageField(
    #     max_length=None,
    #     use_url=True
    # )

    class Meta:
        model = Article
        fields = '__all__'

class DonasiPhotoSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Donasi
        fields = '__all__'
