
Goal Set Track


Notificaciones usuario:

Links para entender en mayor profundidad la metodologia con la que se implemento en esta app: 

Primeros pasos:

Documentacion Oficial

https://docs.djangoproject.com/es/1.10/intro/tutorial01/

Las notificaciones del lado del cliente:

http://stackoverflow.com/questions/11077857/what-are-long-polling-websockets-server-sent-events-sse-and-comet/12855533#12855533

http://stackoverflow.com/questions/6835835/jquery-simple-polling-example

https://github.com/narenaryan/ajaxpost

El envio de mails: Se uso la libreria y servicio sendgrid, que se basa en el protocolo SMTP
	
	https://docs.djangoproject.com/en/1.10/topics/email/

	https://github.com/elbuo8/sendgrid-django

	https://app.sendgrid.com/

	https://es.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol

	http://stackoverflow.com/questions/6367014/how-to-send-email-via-django

	http://stackoverflow.com/questions/6914687/django-sending-email/23402208#23402208

Las queries:

http://stackoverflow.com/questions/24211293/django-queryset-filter-gt-lt-gte-lte-returns-full-object-list	

En el siguiente link, en una de las respuestas se listan todos los operadores, algo muy util

http://stackoverflow.com/questions/687295/how-do-i-do-a-not-equal-in-django-queryset-filtering

https://docs.djangoproject.com/en/1.10/topics/db/queries/

https://docs.djangoproject.com/es/1.10/ref/models/querysets/


Decisiones de Diseño:

Se decidio tener una aplicacion fuertmente modularizada, para que cada clase en lo posible represente un objeto del diseño
original. Las ventajas, fue que al tener alta cohesion, fue relativamente facil adaptarse a los nuevos cambios de la entrega dos,
especialmente en las notificaciones. Por esta razon, se decidio (salvo en el modulo usuario ya que fue la unica forma que nos salio hacer)
que se implementaran las views y las forms de la forma funcional, es decir de la que no se declaran tantas clases, como se puede observar en el modulo
meta o en todos menos usuario como se explico.
Una mala decision de diseño fue la de usar las url en texto plano, o explicitas, eso hizo que tuvieramos muchos conflictos y nos hizo perder tiempo encontrando
errores.
Se decidio hacer las notificaciones con polling ajax, a traves de json por que fue la manera mas simple que se encontro para realizar tal funcionalidad.
El envio de mails se realizo con sendgrid porque fue la mejor forma que se encontro para tal tarea.
En general, se trato de elegir la opcion mas simple, de realizar consultas en lugar de obtener la informacion iterando excplicitamente, 
y si trato en general, de hacer cada funcion muy simple y modularizada. Las notificaciones se realizaron en el modulo meta, y en este modulo
se creo un archivo helpers.py para funciones auxiliares para modularizar y simplificar las funciones de notificaciones y emails.
Todos los comentarios, nombres de funciones, clases y variables estan en español, y son amigables, es decir, su nombre representan lo que hacen.
Los templates tambien se modularizaron para mayor facilidad en la implementacion de las urls.
En general, creo que se realizo un buen proyecto y la aplicacion satisface los requerimentos .