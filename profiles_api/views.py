from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers




# Create your views here.
class HelloApiView(APIView):
    """Test API VIEW"""
    serializer_class=serializers.HelloSerializer

    def get(self, request, format=None):
        """Resturns a list of APIView features"""
        an_apiview=[
        'Uses HTTP methods as functions(get,post,put,delete,patch)',
        'Is similar to a traditional Django View',
        'Gives you the most control over you applications logic',
        'Is mapped manually to URLS',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """hello message with our name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(

            serializer.errors,
            status=status.HTTP_404_BAD_REQUEST
            

            )
