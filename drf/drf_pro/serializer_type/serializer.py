from rest_framework import serializers
from .models import Items, Score

class ItemListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        items = [Items(**item) for item in validated_data]
        return Items.objects.bulk_create(items)

    
    def update(self, instance, validated_data):
        item_mapping = {item.id: item for item in instance}
        data_mapping = {item_data['id']: item_data for item_data in validated_data}

        ret = []
        for item_id, data in data_mapping.items():
            item = item_mapping.get(item_id, None)
            if item is not None:
                for attr, value in data.items():
                    setattr(item, attr, value)
                item.save()
                ret.append(item)
            else:
                ret.append(Items.objects.create(**data))

        return ret

    
class ItemModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Items
        fields = '__all__'
        list_serializer_class = ItemListSerializer

class ScoreSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        score = data.get('score')
        player_name = data.get('player_name')

        if score is None:
            raise serializers.ValidationError('score is required')
        if player_name is None:
            raise serializers.ValidationError('player_name is required')
        return {'score': score, 'player_name': player_name}
    
    def to_representation(self, instance):
        return {
            'score': instance.score,
            'player_name': instance.player_name
        }

    def create(self, validated_data):
        return Score.objects.create(**validated_data)
