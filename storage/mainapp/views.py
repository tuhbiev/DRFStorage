from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import *
from .serializers import *



#Products view
class ProductAPIList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ProductAPIUpdate(generics.RetrieveUpdateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )
    #authentication_classes = (TokenAuthentication,)

class ProductAPIDestroy(generics.RetrieveDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )


#Category view
class CategoryAPIList(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class CategoryAPIUpdate(generics.RetrieveUpdateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

class CategoryAPIDestroy(generics.RetrieveDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )


#Price view
class PriceAPIList(generics.ListCreateAPIView):

    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class PriceAPIUpdate(generics.RetrieveUpdateAPIView):

    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication, )

class PriceAPIDestroy(generics.RetrieveDestroyAPIView):

    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = (IsAdminOrReadOnly, )