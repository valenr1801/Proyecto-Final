from ejemplo.models import Familiar
Familiar(nombre="Valentina", direccion="Córdoba", numero_pasaporte=43144179, fecha_nacimiento="2001-1-18").save()
Familiar(nombre="Fabrizio", direccion="Córdoba", numero_pasaporte=41225727, fecha_nacimiento= "1998-8-10").save()
Familiar(nombre="Antonella", direccion="Córdoba", numero_pasaporte=45595053, fecha_nacimiento= "2004-5-4").save()
print("Se cargo con éxito los usuarios de pruebas")


from ejemplo.models import Mascota
Mascota(propietario= "Valentina", nombre="Simón", raza="Beagle").save()
Mascota(propietario= "Fabrizio", nombre="Timo", raza="Mestizo").save()
Mascota(propietario= "Antonella", nombre="Odie", raza="Mestizo").save()
print("Se cargo con éxito las mascotas de pruebas")

from ejemplo.models import Auto
Auto(propietario= "Valentina", modelo= "Peugeot").save()
Auto(propietario= "Fabrizio", modelo= "Nissan").save()
Auto(propietario= "Antonella", modelo= "Renault").save()
print("Se cargo con éxito los autos de pruebas")
