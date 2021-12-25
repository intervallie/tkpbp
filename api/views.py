from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from accounts.models import Account, BioPsikolog
from article.models import Article
from quiz.models import suggestion
from konfirmasi.models import Konsultasi
from donation.models import Donasi
from django.http import HttpResponse
from django.http import FileResponse
from rest_framework import generics

from consultation_form.models import Consultation
from .serializers import *

User = get_user_model()
# Create your views here.

class IsPsikolog(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_counselor:
            return True
        return False

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims
        token['name'] = user.name
        if user.is_counselor:
            token['domisili'] = user.biopsikolog.domisili
            token['bio'] = user.biopsikolog.bio
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class KonfirmasiAPI(APIView):
    """
    View to list all consulation models that is made for a counselor.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            user_data = User.objects.filter(id=request.user.id).first()
            status_code = status.HTTP_201_CREATED
            if not user_data.is_counselor:
                status_code = status.HTTP_401_UNAUTHORIZED
                response = {
                'status code': status_code,
                'detail': 'Hanya akun psikolog yang dapat mendapatkan list klien',
                }
            else:
                fields = [f.name for f in Consultation._meta.get_fields()]
                fields.remove('selected_counselor')
                data = user_data.consultation_set.all().values(*fields)
                response = {
                    'success': 'true',
                    'status code': status_code,
                    'message': 'Client List fetched successfully',
                    'data': data
                }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Something happened',
                'error': str(e)
                }
        return Response(response,status = status_code)
    
    def post(self,request):
        try:
            full_name = request.data['full_name']
            npm = request.data['npm']
            date = request.data['date']
            email = request.data['email']
            new_konfirmasi = Konsultasi.objects.create(
                full_name = full_name,
                npm = npm,
                date = date,
                email = email,
            )
            Consultation.objects.get(pk=request.data['consultation_id']).delete()

            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Konsultasi created successfully',
                'data' : request.data
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Something happened',
                'error': str(e)
                }
        return Response(response,status = status_code)
    def delete(self,request):
        try:
            Consultation.objects.get(pk=request.query_params['consultation_id']).delete()
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Consultation request successfully deleted (rejected)',
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Something happened',
                'error': str(e)
                }
        return Response(response,status = status_code)

class ArticleAPI(APIView):
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated & (IsAdminUser | IsPsikolog)]
        return [permission() for permission in permission_classes]


    def get(self,request):
        try:
            fields = [f.name for f in Article._meta.get_fields()]
            fields.remove('photo')
            data = Article.objects.all().values(*fields)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Article List fetched successfully',
                'data': data,
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Something happened',
                'error': str(e)
                }
        return Response(response,status=status_code)
    
    def post(self,request):
        try:
            serializer = ArtikelPhotoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                raise ValueError("Please make an appropriate request body")
            data=serializer.data
            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Article posted successfully',
                'data': data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Something happened',
                'error': str(e)
                }
            return Response(response,status=status_code)
    def delete(self,request,pk = None):
        try:
            print("idnya " + str(pk))
            if pk is None:
                artikel = Article.objects.last()
                pk = artikel.pk
            else:
                artikel = Article.objects.get(pk=pk)
            artikel.delete()
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Article deleted successfully',
                'id' : pk
            }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            print(pk)
            print(Article.objects.all().values())
            response = {
                'success': 'false',
                'status code': status_code,
                'message': 'Something happened',
                'error': str(e)
                }
        return Response(response,status=status_code)

class PhotoAPI(APIView):
    def get(self,request):
        try:
            id_article = int(request.query_params['id']) 
            image = Article.objects.filter(id=id_article).first().photo
            return FileResponse(image)
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Something happened',
                'error': str(e)
                }
        return Response(response,status=status_code)

class SuggestionAPI(APIView):
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get(self,request):
        try:
            data = suggestion.objects.all().values()
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Suggestion List fetched successfully',
                'data': data,
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Something happened',
                'error': str(e)
                }
        return Response(response,status=status_code)
    def post(self,request):
        try:
            saran = request.data['saran']
            new_saran = suggestion.objects.create(Saran=saran)
            new_saran.save()
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Suggestion posted successfully',
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Something happened',
                'error': str(e)
                }
        return Response(response,status=status_code)

class ConsultationAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            kota = request.query_params['domisili'].capitalize()
            list_psikolog = BioPsikolog.objects.filter(domisili=kota).all()
            data = []
            status_code = status.HTTP_200_OK
            for psikolog in list_psikolog:
                data_psikolog = {}
                data_psikolog['user_id'] = psikolog.user.id
                data_psikolog['nama'] = psikolog.user.name
                data_psikolog['bio'] = psikolog.bio
                data.append(data_psikolog)
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Counselor List fetched successfully',
                'data': data,
            } 
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Domisili tidak ditemukan',
                'error': str(e)
                }
        return Response(response,status=status_code)

    def post(self,request):
        try:
            full_name = request.data['full_name']
            npm = request.data['npm']
            date = request.data['date']
            email = request.data['email']
            psikolog = Account.objects.filter(id = request.data['user_id']).first()
            if not psikolog.is_counselor:
                status_code = status.HTTP_400_BAD_REQUEST
                response = {
                'status code': status_code,
                'detail': 'Akun yang dituju bukanlah akun psikolog',
                }
            elif request.user.is_counselor:
                status_code = status.HTTP_401_UNAUTHORIZED
                response = {
                'status code': status_code,
                'detail': 'Akun psikolog tidak dapat melakukan request konsultasi',
                }
            else:
                new_consultation = Consultation.objects.create(full_name=full_name,npm=npm,date=date,email=email,selected_counselor=psikolog)
                new_consultation.save()
                status_code = status.HTTP_200_OK
                response = {
                    'success': 'true',
                    'status code': status_code,
                    'message': 'Consultation posted successfully',
                }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Something happened',
                'error': str(e)
                }
        return Response(response,status=status_code)

class DonasiAPI(APIView):
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get(self,request):
        try:
            fields = [f.name for f in Donasi._meta.get_fields()]
            fields.remove('bukti_Transfer')
            data = Donasi.objects.all().values(*fields)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Donation List fetched successfully',
                'data': data,
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Something happened',
                'error': str(e)
                }
        return Response(response,status=status_code)
    
    def post(self,request):
        try:
            serializer = DonasiPhotoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                raise ValueError(serializer.errors)
            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Donation List fetched successfully',
                'data': serializer.data,
            }
            return Response(response, status=status_code)
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Something happened',
                'error': str(e)
                }
            return Response(response,status=status_code)

class MahasiswaAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = []
    serializer_class = RegisterSerializer

class PsikologAPI(generics.CreateAPIView):
    queryset = BioPsikolog.objects.all()
    permission_classes = []
    serializer_class = BioPsikologSerializer





            

            
