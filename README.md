# Código base para inicializar proyecto en django rest

## Este código está pensado para ser usado en Docker, tiene estructura para testing, producción y desarrollo.

//Correr código base

sudo docker-compose -f local.yml  build  #Instalará todos contenedores y sus imágenes

// Correr contenedores docker

sudo docker-compose -f local.yml up

// Saber que contenedores tenemos corriendo

sudo docker-compose -f local.yml ps

// Detener servicio de contenedores que están corriendo

sudo docker-compose -f local.yml stop #Detener 

// Crear variable export para evitar escribir el "local.yml" y escribr solo "docker-compose up...."

export COMPOSE_FILE=local.yml

//**COMANDOS DE ADMINISTRACION**\\

++Comando para correr proyecto y al ser finalizado finalizar el servicio++

sudo docker-compose local.yml run --rm django <<COMMAND>>  ## el <--rm> sirve para cerrar el contenedor una vez matado el proceso


++Comando para crear super admin++

sudo docker-compose -f local.yml run --rm django python manage.py createsuperuser ##Creacion del superuser con linea de comando python


//**Habilitar debugger**\\ ||Esto se debe hacer en otra consola, en el mismo instante en que el proyecto esta corriendo

sudo docker-compose -f local.yml up

sudo docker-compose -f local.yml ps

sudo docker rm -f <ID>  ## Matamos contenedor django

sudo docker-compose -f local.yml run --rm --service-ports django ## comando <<--rm>> para que cuando termine muera el contenedor; <<--service-ports>> para exponer los puertos

