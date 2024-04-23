from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from core.serializer import ClientSerializer 

from core.models import *

@api_view(['POST'])
def create_cliente(request):

    name = request.data.get("name")
    cnpj =request.data.get("cnpj")

    serializer = ClientSerializer(data={'name': name, 'cnpj': cnpj})

    if serializer.is_valid():
        serializer.save()
        return Response({"message":"created"}, status=status.HTTP_201_CREATED)
    
    return Response({"message":"invalid"}, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET'])
def get_client(request):

    client_name = request.query_params.get('name')

    client = Client.objects.filter(name=client_name)

    return Response(ClientSerializer(client.first(), many=False).data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_client(request):

    client_id = request.query_params.get('id-client')
    update_client = Client.objects.filter(id=client_id).first()
    print(client_id)

    if not update_client:
        return Response({"message": "client not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ClientSerializer(update_client, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "updated successfully"}, status=status.HTTP_200_OK)

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
