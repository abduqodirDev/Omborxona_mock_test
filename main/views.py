from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import View

from .models import Product, Material, Product_Material
from .serializers import OmborxonaSerializer, MaterialSerializer, ProductSerializer


class OmborxonaView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = OmborxonaSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        omb_serializer = OmborxonaSerializer(data=data)
        omb_serializer.is_valid(raise_exception=True)
        omb_data = omb_serializer.data
        print("data:", omb_data)


        material_data = []
        pro_count = omb_data.get('quantity', None)
        product = Product.objects.get(name=omb_data.get('product_name', None))
        all_materials = product.materials.all()

        for material in list(all_materials):
            product_material = Product_Material.objects.get(product_id=product.id, material_id=material.id)
            if product_material.quantity*pro_count > material.quantity:
                just_json = {
                    "warehouse_id": None,
                    "material_name": material.name,
                    "qty": product_material.quantity * pro_count,
                    "price": None
                }
                material_data.append(just_json)
                continue

            just_json = {
                "warehouse_id": material.id,
                "material_name": material.name,
                "qty": product_material.quantity*pro_count,
                "price": material.price
            }

            material_data.append(just_json)

        product_data = {
            "product_name": omb_data.get('product_name', None),
            "product_qty": omb_data.get('quantity', None),
            "product_materials": material_data
        }

        return Response({"result": product_data})

