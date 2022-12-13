from django.shortcuts import render , get_object_or_404
from ejemplo.models import Familiar , Mascota , Auto
from ejemplo.forms import Buscar , FamiliarForm, MascotaForm , AutoForm # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT 

def index(request):
    return render(request, "ejemplo/saludar.html")

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):
  form_class = Buscar
  template_name = 'ejemplo/buscar.html'
  initial = {"nombre":""}
  def get(self, request):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form':form})
  def post(self, request):
    form = self.form_class(request.POST)
    if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
            return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/alta_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

  def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

  def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":"", "fecha_nacimiento":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"Se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'
 
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares= Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})

#MASCOTA

def mostrar_mascota(request):
  lista_mascota = Mascota.objects.all()
  return render(request, "ejemplo/mascota.html", {"lista_mascota": lista_mascota})

class BuscarMascota(View):
  form_class = Buscar
  template_name = 'ejemplo/buscar_mascota.html'
  initial = {"nombre":""}
  def get(self, request):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form':form})
  def post(self, request):
    form = self.form_class(request.POST)
    if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_mascota = Mascota.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_mascota':lista_mascota})
            return render(request, self.template_name, {"form": form})

class AltaMascota(View):
  form_class = MascotaForm
  template_name = 'ejemplo/alta_mascota.html'
  initial = {"propieatrio":"", "nombre":"", "raza":""}

  def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

  def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con éxito la mascota {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarMascota(View):
  form_class = MascotaForm
  template_name = 'ejemplo/actualizar_mascota.html'
  initial = {"propietario":"", "nombre":"", "raza":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(instance=mascota)
      return render(request, self.template_name, {'form':form,'mascota': mascota})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(request.POST ,instance=mascota)
      if form.is_valid():
          form.save()
          msg_exito = f"Se actualizó con éxito la mascota {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'mascota': mascota,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


  #AUTO
def mostrar_auto(request):
  lista_auto = Auto.objects.all()
  return render(request, "ejemplo/auto.html", {"lista_auto": lista_auto})

class BuscarAuto(View):
  form_class = Buscar
  template_name = 'ejemplo/buscar_auto.html'
  initial = {"modelo":""}
  def get(self, request):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form':form})
  def post(self, request):
    form = self.form_class(request.POST)
    if form.is_valid():
     nombre = form.cleaned_data.get("nombre")
    lista_auto = Auto.objects.filter(modelo__icontains=nombre).all() 
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form':form, 
                                                        'lista_auto':lista_auto})
    return render(request, self.template_name, {"form": form})

class AltaAuto(View):
  form_class = AutoForm
  template_name = 'ejemplo/alta_auto.html'
  initial = {"propieatrio":"", "modelo":""}

  def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

  def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con éxito el nuevo auto {form.cleaned_data.get('modelo')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarAuto(View):
  form_class = AutoForm
  template_name = 'ejemplo/actualizar_auto.html'
  initial = {"propietario":"", "modelo":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      auto = get_object_or_404(Auto, pk=pk)
      form = self.form_class(instance=auto)
      return render(request, self.template_name, {'form':form,'auto': auto})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      auto = get_object_or_404(Auto, pk=pk)
      form = self.form_class(request.POST ,instance=auto)
      if form.is_valid():
          form.save()
          msg_exito = "Se actualizó con éxito el auto"
          form = self.form_class(initial=self.initial)
      return render(request, self.template_name, {'form':form, 
                                                      'auto': auto,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})
