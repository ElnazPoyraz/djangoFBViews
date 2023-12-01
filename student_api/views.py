from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def home(request):
    return Response({"home":"this is home page"})


@api_view(['GET'])
def butun_ograncileri_getir(request):
    ogrenciler_queryset_tipinde_data = Student.objects.all()
    # print(ogrenciler_queryset_tipinde_data)
    tip_donusumu = StudentSerializer(ogrenciler_queryset_tipinde_data, many=True)
    return Response(tip_donusumu.data)


@api_view(['POST'])
def yeni_ogrenci_create_et(request):
    json_formatin_queryset_donum = StudentSerializer(data=request.data)
    if json_formatin_queryset_donum.is_valid():
        json_formatin_queryset_donum.save()
        return Response(json_formatin_queryset_donum.data, status=status.HTTP_201_CREATED)
    return Response(json_formatin_queryset_donum.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view()
def tek_ogrenciyi_goruntuleme_islemi(request, pk):
    # try:
    #     tek_ogrenci = Student.objects.get(id=pk)
    #     serializer = StudentSerializer(tek_ogrenci)
    #     return Response(serializer.data)
    # except:
    #     return Response({"message": "olmayan id numarasi girildi. id numarani kontrol et!!!"})
    
    tek_ogrenci = get_object_or_404(student, id=pk)
    serializer = StudentSerializer(tek_ogrenci)
    return Response(serializer.data)



@api_view(['PUT'])
def ogrenciyi_guncelle(request, pk):
    tek_ogrenci = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=tek_ogrenci, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def ogrenci_sil(request, pk):
    tek_ogrenci = get_object_or_404(Student, id=pk)
    tek_ogrenci.delete()
    data = {"message": "ogrenci silindi"}
    return Response(data)
