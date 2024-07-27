#motos_api/views.py
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Moto
from .serializers import MotoSerializer

# Create your views here.
# First endpoint view; HTTP methods: GET-All Records POST-New Record


class MotoListApiView(APIView):

    #1. Lista todos los registros
    def get(self, request, *args, **kwargs):
        # List all the moto items for given requested user
        motos = Moto.objects
        serializer = MotoSerializer(motos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #2. Crea un nuevo registro
    def post(self, request, *args, **kwargs):
        # Create the moto with given moto data
        data = {
            'trademark': request.data.get('trademark'),
            'model': request.data.get('model'),
            'reference': request.data.get('reference'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        serializer = MotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Second endpoint view. HTTP method:    GET-Read Records
#                                       PUT-Update Records
#                                       DELETE-Delete Records
class MotoDetailsApiView(APIView):

    # 1. Método auxiliar para obtener el objeto con moto_id dado
    def get_object(self, moto_id):
        try:
            return Moto.objects.get(id=moto_id)
        except Moto.DoesNotExist:
            return None
        
    # 2. Recupera el elemento Moto con moto_id dado
    def get(self, request, moto_id, *args, **kwargs):
        moto_instance = self.get_object(moto_id)
        if not moto_instance:
            return Response(
                {"res": "Object with moto id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = MotoSerializer(moto_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 3. Actualiza el elemento Moto con moto_id dado, si existe
    def put(self, request, moto_id, *args, **kwargs):
        moto_instance = self.get_object(moto_id)
        if not moto_instance:
            return Response(
                {"res": "Object with moto id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'trademark': request.data.get('trademark'),
            'model': request.data.get('model'),
            'reference': request.data.get('reference'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        serializer = MotoSerializer(
            instance = moto_instance,
            data=data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 4. Elimina el elemento Moto con moto_id dado, si existe
    def delete(self, request, moto_id, *args, **kwargs):
        moto_instance = self.get_object(moto_id)
        if not moto_instance:
            return Response(
                {"res": "Object with moto id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        moto_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    

# Clase usada para mostrar el listado de motos (READ)

class MotoListView(View):
    
    def get(self, request):

        # Llamamos todos los objetos de nuestro modelo moto

        motos = Moto.objects.all()

        # Guardamos dentro de contexto la variable motos, donde almacenamos toda la información del modelo

        context = {
            'motos': motos
        }

        # Utilizamos render para el procesamiento de plantillas HTML, le pasamos el respectivo template
        return render(request, 'read.html', context)
    
# Clase usada para crear una nueva moto (CREATE)

class MotoCreateView(View):

    def get(self, request):

        # Renderizamos la vista create.html cuando encuentre esta clase

        return render(request, 'create.html')
    
    # Utilizamos un método en el formulario el cuál nos servirá para poder controlar los datos que se mandan

    def post(self, request):

    # Procedemos a guardar o recuperar los datos según el name del form encontrado

        # Variable                   # Name del form
        reference = request.POST.get('reference')
        trademark = request.POST.get('trademark')
        model = request.POST.get('model')
        price = request.POST.get('price')
        # Lo obtenemos como FILE ya que aquí estamos guardando un archivo
        image = request.FILES.get('image')
        supplier = request.POST.get('supplier')

        # Almacenamos los datos en una variable para proceder a guardarlos
        new_moto = Moto(
            reference = reference,
            trademark=trademark,
            model = model,
            price= price,
            image=image,
            supplier=supplier)
        
        new_moto.save()

        # Redireccionamos a nuestro READ

        return redirect('Moto_list')
    
# Clase usada para editar una moto (UPDATE)

class MotoEditView(View):

    def get(self, request, id):
    
    # Similar al dd(). Buscará dentro del modelo por el id que se pasó por medio del button, si no lo encuentra mandará un mensaje de error 
        moto = get_object_or_404(Moto, id=id)

        # Pasamos los datos por medio del contexto, que serán los atributos de Moto según el id que capturamos y el id por separado

        context = {
            'moto': moto,
            'id': id,
        }

        # Renderizamos la vista update.html cuando encuentre esta clase

        return render(request, 'update.html', context)
    
    # Utilizamos un método en el formulario el cuál nos servirá para poder controlar los datos que se mandan

    def post(self, request, id):

        # Volvemos a buscar el id para saber a cuál objeto editar

        moto = get_object_or_404(Moto, id=id)

        # Procedemos a guardar o recuperar los datos según el name del form encontrado

        # Variable                   # Name del form
        reference = request.POST.get('reference')
        trademark = request.POST.get('trademark')
        model = request.POST.get('model')
        price = request.POST.get('price')
        # Lo obtenemos como FILE ya que aquí estamos guardando un archivo
        image = request.FILES.get('image')
        supplier = request.POST.get('supplier')

        # Actualizamos los campos del objeto moto

        moto.reference = reference
        moto.trademark = trademark
        moto.model = model
        moto.price = price
        moto.supplier = supplier

        # Si se cambia la imagen, se actualizará
        if image:
            moto.image = image

        # Caso contrario al CREATE, aquí solo guardamos cambios ya que ya existe el objeto

        moto.save()

        # Redireccionamos a nuestro READ

        return redirect('Moto_list')
    
# Clase usada para borrar una moto (DELETE)

class MotoDeleteView(View):

    def post(self, request, id):

        # Analizamos si en los datos del POST encuentra una variable de action con el valor de delete

        if request.POST.get('action') == 'delete':

            # Buscamos el id que se ha enviado en el modelo Moto

            moto = get_object_or_404(Moto, id=id)

            # Borramos por id
            
            moto.delete()

            # Redireccionamos a nuestro READ

            return redirect('Moto_list')
