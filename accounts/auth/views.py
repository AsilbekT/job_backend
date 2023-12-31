from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from accounts.auth.serializers import RegistrationSerializer
from .serializers import CustomAuthTokenSerializer
from rest_framework import parsers, renderers
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView
from django.core.cache import cache
from rest_framework.exceptions import AuthenticationFailed


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.get(user=account).key
            data['token'] = token
            response = {
                "status": "success",
                "code": 200,
                "message": 'Successfully registered new user.',
                "data": data
            }
        else:
            data = serializer.errors
            response = {
                "status": "error",
                "code": 400,
                "message": 'Invalid registration data.',
                "data": data
            }
        return Response(response)


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser,
                      parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = CustomAuthTokenSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        try:
            token = Token.objects.get(user=user).key
            response_data = {
                "token": token
            }
            response = {
                "status": "success",
                "code": 200,
                "message": 'Authentication successful.',
                "data": response_data
            }
            return Response(response)
        except Token.DoesNotExist:
            raise AuthenticationFailed(
                "Unable to log in with provided credentials.")