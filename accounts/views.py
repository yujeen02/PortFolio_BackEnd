from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer


class ProfileView(APIView):
    renderer_classes = [JSONRenderer]  # JSON 응답만 허용

    def get(self, request):
        profile = Profile.objects.first()
        if profile is None:
            return Response(
                {"detail": "No profile found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
