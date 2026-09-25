from rest_framework.response import Response;
from rest_framework.views import APIView;
from rest_framework import status;

from .models import Product;
from .serializers import ProductSerializer

class ProductListCreateView(APIView):
    def get(self,request):
        products = Product.objects.all();
        serializer = ProductSerializer(products,many=True);
        return Response(serializer.data,status=status.HTTP_200_OK);
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data);
        serializer.is_valid(raise_exception=True);
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(...)
        # else:
        #     return Response(serializer.errors)
        serializer.save();
        return Response(serializer.data,status=status.HTTP_201_CREATED);
    
class ProductDetailView(APIView):
    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk);
        except Product.DoesNotExist:
            return None;
        
    def get(self,request,pk):
        product = self.get_object(pk);
        if product is None:
            return Response({"detail": "Product not found."},status=status.HTTP_404_NOT_FOUND);
        serializer = ProductSerializer(product);
        return Response(serializer.data);
        
    