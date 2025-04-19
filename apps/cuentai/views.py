from rest_framework import viewsets, status
from rest_framework.permissions import  AllowAny
from .serializers import TextEntrySerializer
from .service import CuentAIService
from rest_framework.response import Response

class CuentAIFlowViewSet(viewsets.ViewSet): 
      # ! Quitar esto cuando tengamos los permisos
     permission_classes = [AllowAny]

     def create(self, request):
           serializer = TextEntrySerializer(data=request.data)
           serializer.is_valid(raise_exception=True)
           entry = serializer.validated_data['entry']
           # llamar al servicio?
           flow = CuentAIService().CuentAIFlow(entry)

           # Tiene que devolver un archivo, revisar
           return Response(flow, status=status.HTTP_200_OK)
