<h1 align="center">API Motos</h1>
<p align="center">Aplicación desarrollada en el framework Django basada en la aplicación de APIs, donde por medio de un frontend podemos agregar, actualizar o eliminar elementos dentro de ella</p>

<h2>API REST</h2>
<p>El tupo de API utilizada para este proyecto fue API REST, la cual funciona de la siguiente manera: El cliente envía las solicitudes al servidor como datos. El servidor utiliza esta entrada del cliente para iniciar funciones internas y devuelve los datos de salida al cliente.</p>

<b>Fuentes: https://aws.amazon.com/es/what-is/api/</b>

Obtenemos respuesta de nuestra API para tener acceso a los elementos contenidos en ella, asi como acceso a poder editar cualquier propiedad o directamente eliminarlos, todo esto basandose en la misma fespiesta que nos da esta API</p>

<h2>Requisitos</h2>
<ul>
  <li>Entorno de desarrollo (Visual Studio Code preferiblemente)</li>
  <li>Framework Django (Instalado)</li>
  <li>Consola Git Bash o CMD</li>
  <li>Python</li>
</ul>

<h2>Ejecución de la aplicación</h2>
<p>
  <ol>
  <b><li>Clona el repositorio</li></b>
    <p>Abre tu consola de Github o CMD, a continuación ubicate en la ruta de la carpeta donde vas a clonar el repositorio. Ahora escribe el siguiente comando: </p>
    <pre><code>git clone https://github.com/notlifeboi/stroop-colors.git</code></pre>
  <b><li>Abre el repositorio clonado</li></b>
    <p>Una vez tengas tu repositorio clonado, abrelo desde tu entorno de desarrollo, ya sea Visual Studio Code o Android Studio. Tener en cuenta que ambos entornos tienen sus     independencias que deben ser instaladas para que pueda correr la aplicación</p>
  <b><li>Activa tu entorno virtual</li></b>
  <p>Activamos nuestro entorno virtual, pasando nuestra carpeta venv al prpyecto, a continuacion escribimos el siguiente comando</p>
    <pre><code>nombre_de_tu_venv\Script\activate</code></pre>
    <p>De esta manera, activaremos el entorno virtual para poder correr el proyecto sin problemas</p>
  <b><li>Corre el proyecto</li></b>
    <p>En la misma terminal donde estas trabajando, escribe el siguiente comando dentro de la carpeta motos_app</p>
    <pre><code>python manage.py runserver</code></pre>
  </ol>
</p>

<h2>Funcionamiento de la aplicación</h2>
<p>Conoce las funcionalidades de la aplicación para que te orientes en el código (La mayoria de este está documentado para que sepas qué hace cada cosa)</p>
  <ul>
    <b><li>Main.dart</li></b>
    <p>Se crea la pantalla de carga inicial, y se define el home que en este caso será menu.dart</p>
    <b><li>Menu.dart</li></b>
    <p>Päntalla inicial de nuestra aplicación, con botones de redirección al leaderboard o puntuaciones locales del usuario, coniguración de juego personalizado o iniciar el      juego el modo normal (Vanilla)</p>
    <b><li>Juego.dart</li></b>
    <p>Se presenta esta pantalla iniciando el juego de modo normal o de manera personalizada, ya que ambas redirecciones contienen los mismos parámetros, aquí se almacenan        varias vistas que se mostrarán si has o no has empezado el juego todavia o si lo has terminado</p>
    <b><li>Leaderboard.dart</li></b>
    <p>Lista de los 5 mejores puntajes guardados de manera local, estos son sobreescritos cuando reinicias la aplicación</p>
    <b><li>Config.dart</li></b>
    <p>En esta pantalla (que es un drawer) Encontrarás inputs para que configures el juego a tu gusto, siendo dos de estos inputs también configurables para el juego en modo       contrarreloj</p>
    <b><li>Contrarreloj.dart</li></b>
    <p>Similar a juego pero no se incluye la variable de intentos, ya que este modo de juego funciona según la cantidad de tiempo que se haya escrito en la configuración, al      llegar el contador a 0, se acabará la partida no importa cuánto te equivoques</p>
    <b><li>Providers/counter_providers.dart</li></b>
    <p>Utilizamos providers para cambiar y almacenar nuevos datos que se registran en el juego personalizado, cuando escribas una configuración, la aplicación se asegura de       guardarla por si quieres volver a empezar tu juego personalizado con la misma configuración. A su vez, guarda y almacena todos los registros de puntuación para 
    después ordenarlo de mayor a menor, ningún puntaje se sobreescribirá   
    menor</p>
  </ul>




