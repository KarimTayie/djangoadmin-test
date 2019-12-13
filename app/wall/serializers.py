from rest_framework import serializers

from core.models import Wall


class WallSerializer(serializers.ModelSerializer):
    """Serializer for wall objects"""
    # user = serializers.CharField(max_length=255)
    username = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        source='user'
    )

    class Meta:
        model = Wall
        fields = ('id', 'username', 'title', 'body')
        read_only_fields = ('id',)
