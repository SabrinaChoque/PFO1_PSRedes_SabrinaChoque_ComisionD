PFO1_PSRedes_SabrinaChoque_ComisionD

Alumno: Sabrina Choque

Comision: D

gitHub: https://github.com/SabrinaChoque/PFO1_PSRedes_SabrinaChoque_ComisionD


Descripcion del PFO1:

El objetivo de este proyecto es crear un sistema simple de comunicación "cliente y servidor". Lo que realizamos es crear archivos servidor, cliente y ver_db. 
Con esto realizaremos la conexión, podremos enviar y recibir mensajes entre servidor y cliente, también se guardará en una base de datos los mensajes y también debemos registrar con fecha, hora e IP.

Los archivos utilizados en Python son:
servidor.py: recibe los mensajes, los guarda en la base de datos y responde al cliente.
cliente.py: se conecta al servidor, envía mensaje y finaliza al escribir la palabra "éxito".
ver_db.py: permite que en pantalla se vean los mensajes guardados como una base de datos.
mensajes.db: este archivo es la base de datos que se genera automáticamente.

Para ejecución y ver debemos realizar los siguientes pasos:
1. Abriremos tres terminales en la carpeta del proyecto.
2. En cada una de las terminales debemos iniciar cada terminal para su respectiva prueba:
En servidor.py :
![servidor]({B6D87536-B228-4050-B122-B558D21F754D}.png)
En cliente.py:
![cliente]({1A288818-0EB9-4895-B705-7136A0A8D4FC}.png)
En ver_db.py:
![ver_db ]({D451958D-DFDA-418D-A3CF-9615AD7809BD}.png)
3. Una vez inicializados en cliente.py, escribiremos los mensajes al servidor, este estará a su vez recibiendo desde servidor.py y se mostrará en ver_db.py:
terminal cliente:
![hola_cliente]({03686B85-BB08-4A5E-A75D-5BF9041A5B86}.png)
terminal servidor:
![respuesta_servidor]({5C665711-CDCD-4583-B7A8-3E6842780592}.png)
terminal ver_db:
![mensajeGuardado_ver_db]({EE32B788-B370-4DEE-883F-8F4028A7D067}.png)
4. Como vemos en las imágenes, los servidores funcionan. Para finalizar simplemente escribimos "éxito" y saldrá lo siguiente:
cliente :
![interactuandoYfinalizando_cliente]({47E3D740-E835-427E-85E3-FE2CCEAB630D}.png)
servidor:
![ultimasInteracciones_servidor]({01F62F1A-6261-4841-91E7-A26F6B924CE4}.png)
ver_db:
![mensajesGuardados_ver_db]({4FFDF837-6A95-4CF8-8BF6-84E1C7F96954}.png)
5. Cuando queramos volver a abrir el servidor solo ingresamos de nuevo en cliente con "python cliente.py", y en servidor nos brindará un nuevo cliente conectado:
![nuevo_clienteEnServidor](image.png)

Con este trabajo práctico entendimos cómo funciona la comunicación cliente-servidor con sockets en Python y cómo se pueden guardar los mensajes en una base de datos para consultarlos después.