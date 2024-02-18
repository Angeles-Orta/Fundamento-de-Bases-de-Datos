FUNDAMENTO DE BASES DE DATOS
Practica 1. Inventario de una farmacia usando python y excel.
Alumnos: 
    -Orta Castillo Maria de los Angeles  No. Cuenta: 319074253
    -Moreno Castro Fernanda  No. Cuenta: 319128727

Requisitos para la compilacion del programa:
    -Python3
    -Pandas version 2.0.0 

Comandos para compilar: "python3 nombre_del_archivo.py"
    *Considere que en la terminal ya debe estar en la carpeta en donde se encuentre el archivo correspondiente*

Sobre el programa: 
El programa trabaja de manera que nos da en primera instancia el inventario de los produtos existentes en la base de datos, 
seguido de esto vienen las opciones de lo que se puede hacer en el programa, que es: 
    1. Agregar artículo - Agregar un nuevo producto, su precio y las cantidades del producto.
    2. Buscar artículo - Nos da la informacion solamente del producto requerido. (Escribe nombre del producto en terminal)
    3. Vender artículo - Aqui se agregan las ventas de los productos asi como cuantos de estos fueron vendidos para que el 
                         inventario sea actualizado.
    4. Ver inventario - Ver las nuevas actualizaciones en el inventario de acuerdo a las opciones anteriores.
    5. Ver ventas - Ver cuanto se ha vendido al dia.
    6. Añadir cantidad en existencia - Añade en el inventario mas cantidad de productos en caso de que se vayan acabando.
    7. Salir - Termina el programa.


Cuestionario: 
1. Describe los principales problemas si se guardara la información en un archivo de
texto cuando deseamos:
    ● Buscar un registro específico en el archivo.
        El problema mas grade es la complejidad, ya que al no estar diseñado para manejar con demasiada informacion
        seria demasiado lento pues buscaria de linea en linea hasta llegar a la informacion deseada, asi como tambien puede 
        ser propenso a errores tanto por la indexacion, la cantidad de informacion y la estructura.
    ● Agregar nuevos productos.
        El principal poblema seria mantener la integridad de os datos, ya que no se podria asegurar que no existan
        datos duplicados o incosnsitencias en la integridad de datos.
        La capacidad de soportar la informacion, pues al manejar cantidades increiblemente enormes de datos podria pasar
        que el archivo de texto simplememte ya no pueda procesarlo pues esta diseñado para un uso mas limitado.

2. ¿Que problemas tuviste para visualizar los datos?
    La pregunta es algo ambigua, aunque poria decir que tal cual no hubo un gran problema paara visualizarlos
    ya que trabajamos con una pequeña cantidad de datos.

3. ¿Es bueno usar hojas de cálculo para guardar la información?
    Si, sin embargo esto puede depender de las necesidades de cada persona, quiza para este ejercicio funciono 
    porque no trabajamos con tanta infromacion al hacer un inventario de pequeño tamaño, pero al tener limitaciones 
    de proceso de infromacion, capacidad, etc. No seria la mejor opcion si querenos trabjar con demasiada informacion.

4. ¿Qué diferencias existen entre una base de datos y una hoja de cálculo?
        - La estructura, las bases de datos estand diseñadas para tener cuertas estructuras que sean mas optimas
        y eficientes de menra que todo esta conectado para su mejor funcionamiento a diferencia de las hojas de calculo,
        en donde, solo puedes hacer una tabla y esta no puede relacionarse con mas cosas para que sea mas funcional.
        - Capacidad: Las bases de datos soportar y manejan cantidades ridiculamente enormes de informacion, mientras que las 
        hojas de datos solo tienen capacidad de manejo para una cantidad muy limitada de informacion.
        - Tiempo: Las bases de datos tienen una velocidad de consulta demasiado rapida, esto debido a las relaciones,
        implementacion y estructuras que se usan para que la complejidad sea la menor posible, mientras que las hojas de 
        calculo tardan bastante tiempo en comparacion pues estas simplemente van de linea en inea hasta encontrar el dato requerido.


5. ¿Qué complejidad tienen las consultas en una hoja de cálculo y en una base de datos?
    Las complejidades son muy distintas pues la de una hoja de calculo puede ser muy lenta ya que va de linea en linea sin embargo,
    es de esperarse pues esta diseñada para trabajar con cantidades "pequelas" de informacion si asi lo podemos decir, asi que su 
    complejidad es lineal aunque esto depende mucho pues si tiene mas camtidad de datos que pueda manejar podria incluso fallar.
    Mientras que una base de datos tiene una complejidad logaritmica, pues justamente esta diseñada para tener consultas rapidas 
    pues trabaja con cantidades enormes de informacion, siendo diseñado para tener consultas complejas.   

6. ¿Cuál fue el primer sistema manejador de base de datos que se creó?
    El primer sistema manejador de bases de datos fue el Sistema de Manejo de Archivos (File Management System), 
    que surgio en la década de 1960. Proporcionaba una manera de almacenar y organizar datos de manera más eficiente 
    que simplemente guardarlos en archivos de texto plano.

7. ¿Qué otro tipo de sistemas persistentes se te ocurren?
    - Sistemas de archivos distribuidos: Permite el almacenamiento y recuperacion de archivos en  redes de computadoras ditribuidas.
    - Almacenes de Datos: Diseñados para el almacenamiento y análisis de grandes cantidades de datos, las cuales ofrecen 
    capacidades avanzadas para consultas analíticas y minería de datos.
    -Sistemas de archivos: Gestionan el almacenamiento y la recuperación de archivos en un sistema informático.

8 .¿En qué casos las hojas de cálculo son buenas para guardar información?
    -Manejo de pequeñas cantidades de datos.
    -Analisis Ad hoc.
    -Colaboracion y comparticion rapida.
    -Pototipo rapido.


