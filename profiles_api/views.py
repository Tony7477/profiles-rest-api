from rest_framework.views import APIView
from rest_framework.response import Response




# Create your views here.
class HelloApiView(APIView):

    """Test API VIEW"""
    def get(self, request, format=None):
        """Resturns a list of APIView features"""
        an_apiview=[
        'Uses HTTP methods as functions(get,post,put,delete,patch)',
        'Is similar to a traditional Django View',
        'Gives you the most control over you applications logic',
        'Is mapped manually to URLS',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
