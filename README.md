# Proyecto-Final
Mi proyecto final
SEED DATA
Dentro de seed_data, encontramos nuestra base de datos original
 Para importar esta base de datos, debemos hacer:
   *python manage.py migrate
   *python manage.py runserver
   *python manage.py shell
   *python manage.py import seed_data
   Si nos aparecen los mensajes que dicen "todos los familiares, autos, y mascotas de pruebas han sido cargados correctamente", está listo.

FORMS
Dentro del archivo forms , se encuentran los formularios según cada clase , en este caso, Familia, Auto y Mascota. A su vez, en el archivo base.html, encontramos todo los datos necesarios para no tener que repetir en todos los demás archivos el mismo código, y asi, poder optimizarlo.

URLS
Dentro de este archivo, encontramos todos los path o rutas que nos llevan a los sitios que requerimos.

MODELS
Dentro de models, tenemos definidas todas las clases principales de nuestro código.

VIEWS
Dentro de views, tenemos otras clases, que provienen de Forms y de clases padres.