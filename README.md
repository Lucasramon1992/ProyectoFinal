# ProyectoFinal
Proyecto final del curso de Python en Coderhouse
Primero que nada les dejo un link para que vean el fucionamiento de la pagina: https://www.youtube.com/watch?v=Yl_aBjTwEJw
   Esta pagina muestra nuestro emprendimiento familiar, cuenta con algunos botones como "Condiciones de compra", "Nuestra Historia", "Nuestro equipo", "Contacto"
  Todos estos botones nos llevaran a diferentes partes de nuestra pagina explicando nuestra trabajo y la forma en la que trabajamos.
  Tambien hay un boton en forma de imagen, que nos lleva hacia arriba de la pagina, como tambien un campo para buscar productos y que nos cuente cuanto cuesta cada producto y por ultimo tambien cuenta con un boton de "Cerrar Sesion"
  ya que la pagina cuenta con un registro de usuario necesario para el ingreso de la pagina.
  Tambien la pagina cuenta con un superusuario predeterminado que es usuario: admin y contraseña: administrador , ingresando en el, el boton de lista de precio cambia a editar lita de precios de esta manera nos lleva a la misma lista anterior con diferencia que esta se puede editar, eliminar o crear un producto nuevo.
  El models que utilice en este caso es models_productos que se encuentran en la carpeta app1 con el nombre de archivo models.py, el mismo es asociados con el archivo views.py que se encuentra en la carpeta app1 en el se define todo el funcionamiento del programa. Luego el archivo views.py se relaciona con el archivo url.py de la carpeta app1, en el cual encontraremos todas las urls necesarias para utilizar en nuestra pagina, estas urls entan asociadas a los archivos .html . No olviden que para comenzar a utilizar este programa hay que colocar en el terminal "manage.py makemigrations" luego "manage.py migrate" y por ultimo "manage.py runserver" Gracias.
