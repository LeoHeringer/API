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


    if not name:
        return Response({'message': "invalid str"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    if not cnpj:
        return Response({'message': "invalid str"}, status=status.HTTP_400_BAD_REQUEST)
    
    if Client.objects.filter(name=name, cnpj=cnpj).exists():
        return Response({"message":"exists"}, status=status.HTTP_400_BAD_REQUEST)


    if name and cnpj:
        Client.objects.create(name=name, cnpj=cnpj)
        return Response({"message":"create"}, status=status.HTTP_200_OK)
    
    return Response({"message":"invalid"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_vehicle_id(request: Request) -> Response:
    
    veihcle_placa = request.data.get('placa')
    veihcle_model = request.data.get('model')
    veihcle_client_id = request.data.get('client_id')
    
    if not veihcle_placa:
        return Response({"message": "Placa invalid"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not veihcle_model:
        return Response({"message": "Model invalid"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not Client.objects.filter(id=veihcle_client_id).exists():
        return Response({"message": "Client not found"}, status=status.HTTP_400_BAD_REQUEST)

    if not veihcle_client_id:
        return Response({"message": "Client ID invalid"}, status=status.HTTP_400_BAD_REQUEST)
    
    client = Client.objects.filter(id=veihcle_client_id).first()
    Vehicle.objects.create(placa=veihcle_placa, model=veihcle_model, client=client)

    return Response({"message": "CLient created successfully"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def create_veihcle_name(request: Request) -> Response:

    veihcle_placa = request.data.get('placa')
    veihcle_model = request.data.get('model')
    client_name = request.data.get('name')

    if not veihcle_placa:
        return Response({"message": "Placa invalid"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not veihcle_model:
        return Response({"message": "Model invalid"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    if Client.objects.filter(name = client_name).exists():
        return Response({"message": "Client not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not client_name:
        return Response({"message": "Client invalid"}, status=status.http)


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


    if not name or not cnpj:
        return Response({"message":"invalid"}, status=status.HTTP_400_BAD_REQUEST)

    update_client.name = name
    update_client.cnpj = cnpj
    update_client.save()
    return Response({"message": "updated successfully"}, status=status.HTTP_200_OK)
    


@api_view(['DELETE'])
def delete_client(request):

    client_id = request.query_params.get('id-client')
    delete_to_client = Client.objects.filter(id=client_id).first()
    

    if delete_to_client:
        serializer = ClientSerializer(delete_to_client)
        delete_to_client.delete()
        return Response({"message": "successfully deleted", "client": serializer.data}, status=status.HTTP_200_OK)

    return Response({"message": "invalid"}, status=status.HTTP_400_BAD_REQUEST)
