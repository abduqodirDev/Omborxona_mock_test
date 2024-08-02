from rest_framework import serializers


class OmborxonaSerializer(serializers.Serializer):
    product_name = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)


class MaterialSerializer(serializers.Serializer):
    warehouse_id = serializers.IntegerField()
    material_name = serializers.CharField()
    qty = serializers.IntegerField()
    price = serializers.DecimalField(decimal_places=2, max_digits=10)


class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    product_qty = serializers.DecimalField(decimal_places=2, max_digits=10)

    product_materials = MaterialSerializer(many=True)

