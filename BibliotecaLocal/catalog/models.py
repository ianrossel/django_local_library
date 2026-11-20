from django.db import models
from django.urls import reverse


class MyModelView(models.Model):
    '''Una clase típica que define un modelo, derivada de la clase Model'''

    # Campos
    my_field_name = models.CharField(max_length=20, help_text = 'Ingrese un valor para este campo')
    #...

    # Metadatos
    class Meta:
        ordering =["my_field_name"]

    # Métodos
    def get_absolute_url(self):
        '''Devuelve la URL para acceder a una instancia particular de MyModelView'''

        return reverse('model-detail-view', args = [str(self.id)])

    def __str__(self):
        '''Cadena para representar el objeto MyModelView (en el sitio Admin, etc)'''

        return self.my_field_name

record = MyModelView(my_field_name='Instancia #1')

record.save()  # Guardar el registro en la base de datos

# Accede a los valores de los campos del modelo usando atributos de Python.
print(record.id) # debería devolver 1 para el primer registro.
print(record.my_field_name) # debería imprimir 'Instancia #1'