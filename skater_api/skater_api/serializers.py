from rest_framework import serializers
from .models import Skater, Tricks

class SkaterSerializer(serializers.HyperlinkedModelSerializer):
    tricks = serializers.HyperlinkedRelatedField(
        view_name='trick_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Skater
        fields = ('name', 'age', 'home_town', 'board_sponser', 'shoe_sponsor', 'photo_url')


class TrickSerializer(serializers.HyperlinkedModelSerializer):
    skater = serializers.HyperlinkedRelatedField(
        view_name='skater_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Tricks
        fields = ('skater', 'trick_name' 'signature_trick', 'favorite_trick', 'trick_location', 'photo_url')