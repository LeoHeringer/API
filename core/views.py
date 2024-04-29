from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from core.serializer import ClientSerializer 

from core.models import *

@api_view(['POST'])
def create_cliente(request):

    name = request.data.get("name")
    cnpj = request.data.get("cnpj")

    if not name.strip() or not cnpj.strip():
        return Response({'message': "invalid str"}, status=status.HTTP_400_BAD_REQUEST)
    
    if Client.objects.filter(name=name, cnpj=cnpj).exists():
        return Response({"message":"exists"}, status=status.HTTP_400_BAD_REQUEST)


    if name and cnpj:
        Client.objects.create(name=name, cnpj=cnpj)
        return Response({"message":"create"}, status=status.HTTP_200_OK)
    
    return Response({"message":"invalid"}, status=status.HTTP_400_BAD_REQUEST)
    
    # if Client.objects.filter(name=name, cnpj=cnpj).exists():
    #     return Response({"message": "exists"}, status=status.HTTP_400_BAD_REQUEST)
        
    # serializer = ClientSerializer(data=request.data)
    
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response({"message":"created"}, status=status.HTTP_201_CREATED)
    
    # return Response({"message":"invalid"}, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET'])
def get_client(request):

    client_name = request.query_params.get('name')

    client = Client.objects.filter(name=client_name)

    return Response(ClientSerializer(client.first(), many=False).data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_client(request):

    client_id = request.query_params.get('id-client')
    update_client = Client.objects.filter(id=client_id).first()
    
    if not update_client:
        return Response({"message": "client not found"}, status=status.HTTP_404_NOT_FOUND)
    

    name = request.data.get('name')
    cnpj = request.data.get('cnpj')

    if name and name.strip() and cnpj.strip():
        update_client.name = name
        update_client.cnpj = cnpj
        update_client.save()
        return Response({"message": "updated successfully"}, status=status.HTTP_200_OK)
    
    # serializer = ClientSerializer(update_client, data=request.data)

    # if serializer.is_valid():
    #     serializer.save()
    #     return Response({"message": "updated successfully"}, status=status.HTTP_200_OK)

    return Response({"message": "invalid"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_client(request):

    client_id = request.query_params.get('id-client')
    delete_to_client = Client.objects.filter(id=client_id).first()
    

    if delete_to_client:
        serializer = ClientSerializer(delete_to_client)
        delete_to_client.delete()
        return Response({"message": "successfully deleted", "client": serializer.data}, status=status.HTTP_200_OK)

    return Response({"message": "invalid"}, status=status.HTTP_400_BAD_REQUEST)
