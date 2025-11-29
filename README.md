"#gitflowBasico3" 

# Django forms

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Item

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tu username',
            'class': 'form-control'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Tu password',
            'class': 'form-control'
        }
    ))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tu Username',
            'class': 'form-control'
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Tu Email',
            'class': 'form-control'
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Repite Tu Password',
            'class': 'form-control'
        }
    ))
```

# Registro de usuarios en views.py
```python
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from .models import Item, Category

from .forms import SignupForm
 

# Create your views here.
def home(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'store/home.html', context)

def contact(request):
    context = {
        'msg': 'Quieres otros productos contactame!'
    }

    return render(request, 'store/contact.html', context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, 
                                        is_sold=False).exclude(pk=pk)[0:3]

    context={
        'item': item,
        'related_items': related_items
    }

    return render(request, 'store/item.html', context)

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    
    context = {
        'form': form
    }

    return render(request, 'store/signup.html', context)
    ```

# Templates de login y signup
```html
{% extends 'store/base.html' %}

{% block title %}Login | {% endblock %}

{% block content %}
<div class="row p-4">
    <div class="col-6 bg-light p-4">
        <h4 class="mb-6 text-center">Login</h4>
        <hr>
        <form action="." method="POST">
            {% csrf_token %}
            <div class="form-floating mb-3">
                <h6>Username:</h6>
                {{ form.username }}
            </div>
 
            <div class="form-floating mb-3">
                <h6>Password:</h6>
                {{ form.password }}
            </div>

            {% if form.errors or form.non_field_errors %}
                <div class="mb-4 p-6 bg-danger">
                    {% for field in form %}
                        {{fiels.errors}}
                    {% endfor %}

                    {{ form.non_field_errors }}
                </div>
            {% endif %}
            <button class="btn btn-primary mb-6">Login</button>

        </form>
    </div>
</div>
{% endblock %}
```

```html
{% extends 'store/base.html' %}

{% block title %}Login | {% endblock %}

{% block content %}
<div class="row p-4">
    <div class="col-6 bg-light p-4">
        <h4 class="mb-6 text-center">Login</h4>
        <hr>
        <form action="." method="POST">
            {% csrf_token %}
            <div class="form-floating mb-3">
                <h6>Username:</h6>
                {{ form.username }}
            </div>
 
            <div class="form-floating mb-3">
                <h6>Password:</h6>
                {{ form.password }}
            </div>

            {% if form.errors or form.non_field_errors %}
                <div class="mb-4 p-6 bg-danger">
                    {% for field in form %}
                        {{fiels.errors}}
                    {% endfor %}

                    {{ form.non_field_errors }}
                </div>
            {% endif %}
            <button class="btn btn-primary mb-6">Login</button>

        </form>
    </div>
</div>
{% endblock %}
```

# Rutas en url's para login y registro de usuarios
```python
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import contact, detail, register

from .forms import LoginForm

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm), name='login'),
    path('detail/<int:pk>/', detail, name='detail'),
]
```

#  Marketplace Main – Documentación del Proyecto  
Proyecto desarrollado con Django, utilizando una arquitectura clara y profesional basada en el patrón **MVT (Model–View–Template)**. Este documento explica el funcionamiento del framework, los comandos utilizados y la estructura interna del proyecto.

---

#  ¿Por qué utilizar Django para desarrollar aplicaciones web?

Django es un framework que ya viene equipado con múltiples herramientas listas para usarse, lo que permite desarrollar aplicaciones de manera más rápida y segura. Algunas de sus ventajas principales son:

### ✔️ **Tiene herramientas integradas**
Permite crear bases de datos, sistemas de login, administración, formularios y seguridad sin tener que crear todo desde cero.

### ✔️ **Es seguro**
Incluye mecanismos para evitar ataques comunes como SQL Injection, CSRF o XSS.

### ✔️ **Es escalable**
Si tu proyecto crece en usuarios y datos, Django puede crecer contigo sin problemas.

### ✔️ **Tiene una estructura ordenada**
Su arquitectura ayuda a organizar archivos, separar responsabilidades y mantener el código limpio. Esto facilita el trabajo en equipo y la resolución de errores.

### ✔️ **Tiene una comunidad enorme**
Miles de tutoriales, foros, documentación y paquetes reutilizables hacen que avanzar sea más sencillo.

### ✔️ **Aumenta tu velocidad de desarrollo**
Django trae funcionalidades listas que te permiten enfocarte en lo importante del proyecto.

> **En pocas palabras:** usar Django es como tener una cocina equipada: solo llegas, cocinas y listo. No tienes que comprar ollas, cuchillos ni nada para empezar.

---

#  Comandos de CMD utilizados

| Nº | Comando | Descripción |
|---|---------|-------------|
| 1 | `cd` | Cambia de directorio. |
| 2 | `md` | Crea una carpeta nueva. |
| 3 | `python -m venv venv` | Crea un entorno virtual aislado. |
| 4 | `dir` | Lista archivos y carpetas del directorio actual. |
| 5 | `venv\Scripts\activate` | Activa el entorno virtual. |
| 6 | `pip install django` | Instala Django. |
| 7 | `django-admin startproject marketplace_main` | Crea un nuevo proyecto Django. |
| 8 | `python manage.py runserver` | Inicia el servidor local. |
| 9 | `python manage.py startapp store` | Crea la app llamada *store*. |
|10 | `python manage.py migrate` | Crea las tablas iniciales de la base de datos. |
|11 | `python manage.py createsuperuser` | Crea un usuario administrador. |
|12 | `python manage.py makemigrations` | Genera migraciones basadas en cambios del modelo. |
|13 | `pip freeze > requirements.txt` | Guarda las dependencias instaladas. |
|14 | `code .` | Abre VSCode en el directorio actual. |

---

#  Arquitectura MVT en Django

La arquitectura **MVT (Model – View – Template)** organiza un proyecto de esta forma:

###  **Model (models.py)**
Define la estructura de los datos que se guardarán en la base de datos.  
Ejemplos: usuarios, productos, categorías, comentarios.

###  **View (views.py)**
Recibe la solicitud del usuario, procesa datos y regresa una respuesta.  
Se comunica con los modelos y renderiza plantillas.

###  **Template (HTML dentro de templates/)**
Es la parte visual: HTML + CSS.  
Muestra la información que las vistas le envían.

**En resumen:**  
*El modelo almacena información, la vista la interpreta y la plantilla la muestra.*

---

#  Archivos principales del proyecto

##  settings.py
Es el archivo de configuración principal del proyecto. Administra:

- Base de datos
- Lista de aplicaciones instaladas
- Idioma y zona horaria
- Archivos estáticos y multimedia
- Seguridad (SECRET_KEY)
- `ALLOWED_HOSTS` y dominios permitidos

Es el núcleo del proyecto.

---

## 📌 urls.py
Dirige las URL a las vistas correspondientes.  
Cuando un usuario escribe un enlace, Django revisa este archivo para saber qué vista ejecutar.

---

## 📌 models.py
Contiene la estructura de los datos del sistema.  
Define:

- tipos de datos
- relaciones
- reglas de la base de datos

Django usa este archivo para crear tablas automáticamente mediante migraciones.

---

## 📌 views.py  
Aquí se define la lógica de la aplicación.  
Procesa solicitudes HTTP, consulta la base de datos y devuelve respuestas.

Vistas más importantes utilizadas:

###  **login()**
Valida credenciales del usuario y permite iniciar sesión.

###  **logout_user()**
Cierra la sesión y borra la información del usuario.

###  **detail()**
Recibe un ID y muestra información detallada sobre un objeto (producto, usuario, etc.).

###  **add_item()**
Opera un formulario para crear un nuevo artículo en la base de datos.

---

#  Decorador LOGIN_REQUIRED

`@login_required` restringe el acceso a ciertas vistas para que solo usuarios autenticados puedan verlas.

Si un usuario no logueado intenta entrar:
- Django lo redirige a la página de login.
- Luego lo devuelve a la página que quería ver.

Es fundamental para proteger páginas sensibles como:
- perfil de usuario
- agregar productos
- editar artículos
- panel administrativo

---

#  urls.py – Vistas conectadas

Cada vista debe aparecer en `urls.py` para poder acceder desde el navegador.  
Ejemplos de rutas agregadas:

- `/contact/`
- `/register/`
- `/detail/<id>/`
- `/logout/`
- `/add_item/`

Sin estar en `urls.py`, una vista no es accesible.

---

# 🎨 Templates (HTML)

Carpeta: **store/templates/store**

###  item.html
Muestra detalles de un producto:
- imagen
- nombre
- precio
- vendedor
- descripción
- botón de contacto

###  login.html
Formulario de inicio de sesión:
- usuario
- contraseña
- manejo de errores
- enlace a registro

###  signup.html
Formulario de registro:
- usuario
- correo
- contraseña y confirmación
- validaciones
- errores

###  navigation.html
Barra de navegación con enlaces dinámicos según si el usuario está logueado o no:
- Home  
- Contact  
- Add Item (solo usuarios logueados)  
- Logout  
- Login / Register  

###  form.html
Plantilla genérica para formularios de Django:
- título dinámico
- errores
- permite subir archivos
- botón de enviar

---

#  forms.py  

Archivo que contiene formularios importantes del proyecto:

###  LoginForm
Basado en `AuthenticationForm`.  
Permite iniciar sesión validando credenciales.

### SignupForm
Basado en `UserCreationForm`.  
Permite crear nuevos usuarios, validando contraseñas y correo.

###  NewItemForm
Un ModelForm para crear artículos de la tienda:
- categoría
- nombre
- descripción
- precio
- imagen

---

#  Categorías del Proyecto

Se crearon las siguientes categorías:

- Anillos  
- Ropa  
- Basquetbol  
- Zapatos  

Cada categoría tiene sus ítems con:
- descripción  
- imágenes  
- precios  

---



---

#  Conclusión

Django es un framework completo, seguro y organizado que facilita la creación de aplicaciones web profesionales. Su arquitectura MVT permite separar la lógica, los datos y la presentación, haciendo que los proyectos sean fáciles de mantener y escalar.

En el desarrollo de **Marketplace Main**, comprendimos la importancia de:
- la estructura del proyecto
- los archivos principales como settings, urls, views y models
- la seguridad del sistema
- el manejo de vistas, formularios y plantillas

Django simplifica tareas complejas y nos brinda las herramientas necesarias para crear aplicaciones web modernas, eficientes y seguras.

---

## 📝 Conclusión

Trabajar con Django me permitió entender cómo funciona realmente una aplicación web desde adentro. Este framework ofrece una estructura muy completa donde cada archivo tiene un propósito claro, lo que hace que el proyecto esté bien organizado y sea más fácil de manejar.  

A lo largo del desarrollo del proyecto **marketplace_main**, pude ver cómo todo se conecta:  
- `settings.py` configura el entorno.  
- `urls.py` dirige las rutas.  
- `models.py` define los datos.  
- `views.py` maneja la lógica.  
- La carpeta `templates` se encarga de la parte visual.  

Gracias a esa división, es más sencillo entender el código, corregir errores y agregar nuevas funciones.  

También me di cuenta de que Django facilita mucho el trabajo porque ya trae herramientas listas, como el sistema de autenticación, los formularios y las migraciones para la base de datos. Esto permitió enfocarnos más en construir la tienda en línea y menos en problemas técnicos.  

En general, este proyecto fue útil para aprender cómo se desarrolla una aplicación real y cómo Django ayuda a que todo sea más seguro, ordenado y escalable. Esta experiencia me dejó más clara la importancia de usar un framework profesional para crear aplicaciones web modernas.

---

