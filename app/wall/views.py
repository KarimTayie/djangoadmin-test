from rest_framework import generics, authentication, permissions

from core.models import Wall

from wall.serializers import WallSerializer


class ListWallPostsView(generics.ListAPIView):
    queryset = Wall.objects.all()
    serializer_class = WallSerializer


class CreateWallPostsView(generics.CreateAPIView):
    serializer_class = WallSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)
