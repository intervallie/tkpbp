from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from article.models import Article
from donation.models import Donasi
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from accounts.models import BioPsikolog

User = get_user_model()

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

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email','name','password1','password2')


    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            is_active = True,
            is_counselor = False,
            is_staff = False,
            is_superuser = False
        )
        user.set_password(validated_data['password1'])
        user.save()

        return user

class BioPsikologSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()

    class Meta:
        model = BioPsikolog
        fields = ('user','domisili','bio',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(
            email=user_data['email'],
            name=user_data['name'],
            is_active = True,
            is_counselor = True,
            is_staff = False,
            is_superuser = False
        )
        bio_counselor = BioPsikolog.objects.create(user = user,domisili = validated_data['domisili'],bio = validated_data['bio'])
        # bio_counselor.user = counselor
        user.set_password(user_data['password1'])
        user.save()
        bio_counselor.save()
        return bio_counselor


