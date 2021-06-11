from rest_framework import serializers
from .models import Skater, Tricks

class SkaterSerializer(serializers.HyperlinkedModelSerializer):
    tricks = serializers.HyperlinkedRelatedField(
        view_name='trick_detail',
        many=True,
        read_only=True
    )

    skater_url = serializers.ModelSerializer.serializer_url_field(
        view_name='skater_detail'
    )
    class Meta:
        model = Skater
        fields = ('id', 'name', 'age', 'home_town', 'board_sponsor', 'shoe_sponsor', 'photo_url', 'skater_url', 'tricks',)


class TricksSerializer(serializers.HyperlinkedModelSerializer):
    # skater = serializers.HyperlinkedRelatedField(
    #     view_name='skater_detail',
    #     many=True,
    #     read_only=True
    # )
    
    # skater_id = serializers.PrimaryKeyRelatedField(
    #    queryset=Skater.objects.all(),
    #    source='tricks'
    #   )

    class Meta:
        model = Tricks
        fields = ('trick_name', 'signature_trick', 'favorite_trick', 'trick_location', 'photo_url')