from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from productregistration.serializer import ProductSerializer


class RegistrationProductApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'price': request.data.get('price')
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
