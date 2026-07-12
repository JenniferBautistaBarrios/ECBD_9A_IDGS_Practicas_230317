## Práctica 04 - Manejo de mapas de calor (Heatmaps) Georeferenciales en el análisis EDA
<center>

<img src="../images/logo_ti.png" width=400px>

### Tecnologías
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&style=flat-square)
![Pandas](https://img.shields.io/badge/pandas-1.0%2B-0e76a8?logo=pandas&style=flat-square)
![NumPy](https://img.shields.io/badge/NumPy-1.18%2B-darkblue?logo=numpy&style=flat-square)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11%2B-4C9ACA?style=flat-square)

</center>




### Descripción
El estudiante pondrá en práctica la realización de un análisis exploratorio de datos con multiples datasets, asi como implementar el uso de mapas de calor con referencia con posicionamiento de GPS, con la finalidad de visualizar las frecuencias y tendencias sobre los datos que requieren una referencia geográfica mundial en su contexto.

DonorsChoose es una organización sin fines de lucro de EE. UU. que permite donar directamente a proyectos de aulas de escuelas públicas. En este notebook se realiza un análisis exploratorio completo del conjunto de datos compartido por DonorsChoose (donantes, donaciones, maestros, escuelas, recursos y proyectos), con el fin de extraer información útil para campañas de correo dirigidas a donantes.

#### 1. Preparación del Conjunto de Datos
Se importan las bibliotecas necesarias (pandas, numpy, seaborn, matplotlib, entre otras) y se cargan los distintos archivos CSV del dataset de DonorsChoose (donantes, donaciones, maestros, escuelas, recursos y proyectos) que se usarán a lo largo de todo el análisis.
<img src="/Practica04/images/1.png">

#### 2. Explorando a los Donantes
#### 2.1 Vista rapida de los Donantes
Existen un total de **2,122,640 donantes** registrados en DonorsChoose hasta abril de 2018, distribuidos en **15,204 ciudades** de Estados Unidos y otros países. Solo el **26% (552,941)** de los donantes ha donado más de una vez, mientras que **1,471,613** donantes solo han donado en una ocasión, lo que representa una oportunidad para motivarlos a donar nuevamente.
<img src="/Practica04/images/2.1.png">


#### 2.2 Donantes de cada Estado
##### 2.2.1 Donantes de cada Estado
California es el estado con más donantes registrados (casi 300,000), destacando San Francisco y Los Ángeles. Nueva York, Texas y Florida le siguen con aproximadamente 137,000, 134,000 y 108,000 donantes respectivamente. Dakota del Norte, Dakota del Sur, Vermont y Wyoming son los estados con menos donantes (menos de 4,000). A nivel de ciudades, Chicago, Nueva York y Brooklyn concentran el mayor número de donantes.
<img src="/Practica04/images/2.2.1.png">

##### 2.2.2 Analisis de Donantes
Este gráfico complementa la vista anterior, mostrando con mayor detalle la distribución y concentración de donantes por estado y ciudad, confirmando el dominio de California, Nueva York, Texas y Florida en el número absoluto de donantes.
<img src="/Practica04/images/2.2.2.png">

#### 2.3 Estados con la mayor Proporción de Donantes por Habitante
Al ajustar por población, Carolina del Sur, Massachusetts y Connecticut son los estados con mayor proporción de donantes por cada 100,000 habitantes (985, 907 y 878 respectivamente). En contraste, Wyoming, Nebraska y Nuevo México tienen la menor proporción. Texas, a pesar de tener muchos donantes en términos absolutos, tiene una proporción baja (508 por cada 100K habitantes).
<img src="/Practica04/images/2.3.png">

#### 2.4 Visualicemos dónde se encuentran los Donantes
##### 2.4.1 Dónde se encuentran los donantes en California
Las ciudades con mayor densidad de donantes en California son Los Ángeles (17,922), San Francisco (16,553), San Diego (9,072), San José (7,674) y Oakland (6,783).
<img src="/Practica04/images/2.4.1.png">

##### 2.4.2 Dónde se encuentran los donantes en Florida
La región tri-condado (Palm Beach, Miami-Dade y Broward) concentra la mayor cantidad de donantes, junto con Tampa. Las principales ciudades son Miami (9,309), Tampa (6,016), Orlando (5,658), Jacksonville (4,598) y Fort Lauderdale (4,311).
<img src="/Practica04/images/2.4.2.png">

##### 2.4.3 Dónde se encuentran los donantes en Nueva York
Los donantes se concentran principalmente en la ciudad de Nueva York (26,820), seguida de Brooklyn (21,715), Staten Island (4,516), Bronx (4,455) y Buffalo (2,232).
<img src="/Practica04/images/2.4.3.png">

##### 2.4.4 Dónde se encuentran los donantes en Texas
Las ciudades principales son Houston (15,404), Austin (9,958), Dallas (7,818), San Antonio (6,465) y Fort Worth (4,350).
<img src="/Practica04/images/2.4.4.png">

#### 2.5 Dónde se encuentran los donantes?
Aunque California concentra el mayor número de donantes, la costa este de EE. UU. muestra una densidad de donantes más alta en comparación con el oeste. También se observa un número significativo de donantes en Hawái y Alaska.
<img src="/Practica04/images/2.5.png">

#### 2.6 numero de donantes maestros y no maestros por estado
El número de donantes que también son maestros es bajo en todos los estados. Los registros clasificados como "otros" concentran el mayor número de donantes maestros, con aproximadamente 28,000.
<img src="/Practica04/images/2.6.png">

#### 3. Exploración de las Donaciones
El archivo de donaciones incluye el monto total donado, la secuencia del carrito del donante, la fecha, el ID del proyecto y el ID del donante.
##### 3.1 Vista rapida de las Donaciones
Se registran un total de **4,687,884 donaciones** hasta abril de 2018. La donación más alta fue de **USD 60,000** (2013). El **83%** de las donaciones son menores a USD 100, y DonorsChoose ha recaudado en total **USD 284,408,243**, con un monto promedio de donación de USD 60.
<img src="/Practica04/images/3.1.png">

#### 3.2 Proyectos y sus Donaciones
El proyecto con más donaciones en la historia de DonorsChoose es "Vallecito StandUpKids Pilot Standing School!" con 863 donaciones y USD 108,248.30 recaudados. El proyecto "Varsity and After-School Fencing Teams in NYC" tuvo el monto promedio más alto por donante (USD 1,850), y "Learning to Play While Playing to Learn!" recibió la donación única más alta de la historia (USD 60,000).
<img src="/Practica04/images/3.2.png">

#### 3.3 Quiénes son los Principales Donantes
Un donante no maestro de Manhattan Beach, California ha realizado más de 18,000 donaciones. Otro donante de Nueva York ha aportado un total de USD 1.8 millones en 10,513 donaciones. El pago único más alto (USD 60,000) fue realizado por un donante de Anahola, Hawái.
<img src="/Practica04/images/3.3.png">

#### 3.4 Qué Montos de Donación se recibieron en qué momentos?
##### 3.4.1 Número de Donaciones por Año
##### 3.4.2 Monto Promedio de Donación por Año
Desde 2012 el número de donaciones ha crecido de forma constante, pasando de ~150 donaciones a cerca de 1.1 millones en 2017. El monto promedio de donación por año ronda los USD 60, siendo más alto en 2012 (USD 166).
<img src="/Practica04/images/3.4.1_3.4.2.png">

##### 3.4.3 Número de Donaciones por Mes
##### 3.4.4 Donaciones Promedio por Mes
Agosto es el mes con más donaciones (577,274), seguido de septiembre (518,908); junio (191,221) y mayo (243,440) son los meses con menos donaciones. Diciembre tiene el monto promedio más alto (USD 80) y julio el más bajo (USD 51).
<img src="/Practica04/images/3.4.3_3.4.4.png">

##### 3.4.5 Número de Donaciones por Día del Mes
##### 3.4.6 Donaciones Promedio por Día del Mes
Se analiza la distribución de donaciones a lo largo de los días del mes, observando patrones relacionados con los ciclos de pago e inicio/fin de mes.
<img src="/Practica04/images/3.4.5_3.4.6.png">

##### 3.4.7 Número de Donaciones por Día de la Semana
##### 3.4.8 Donaciones Promedio por Día de la Semana
El número de donaciones es más alto al inicio de la semana (lunes, martes y miércoles, con 700K, 800K y 750K donaciones aproximadamente) y disminuye hacia el fin de semana, siendo el sábado el día con menos donaciones.
<img src="/Practica04/images/3.4.7_3.4.8.png">

##### 3.4.9 Número de Donaciones por Hora
##### 3.4.10 Donaciones Promedio por Hora
Se examina en qué horas del día se concentran más donaciones y en qué horas los montos promedio son más altos.
<img src="/Practica04/images/3.4.9_3.4.10.png">

#### 3.5 Donaciones Opcionales y Donantes Maestros
##### 3.5.1 Donaciones Opcionales Totales y sus Montos Promedio Asociados
El monto promedio de las donaciones opcionales es de USD 58, frente a USD 73 en donaciones no opcionales. Aproximadamente el 15% de todas las donaciones fueron opcionales.
<img src="/Practica04/images/3.5.1.png">

##### 3.5.2 Donaciones de Donantes Maestros Totales y los Montos Promedio Asociados
Cerca del 29% de las donaciones totales provienen de donantes que también son maestros, siendo California el estado con más donantes maestros. El monto promedio donado por un maestro es de USD 45, frente a USD 66 de donantes no maestros.
<img src="/Practica04/images/3.5.2.png">

#### 3.6 Qué Estados recibieron los Montos de Donación Únicos más Altos
##### 3.6.1 Estados principales con los montos de donación más altos
##### 3.6.2 Ciudades principales con los montos de donación más altos
Hawái y Colorado, aunque con menos donaciones en cantidad, reciben los montos únicos más altos. Las ciudades Anahola, Lafayette y Palo Alto destacan con montos de hasta USD 60K, 31K y 26K.
<img src="/Practica04/images/3.6.png">

#### 3.7 Qué Estado Recibe los Montos de Donación Promedio más Altos
Hawái y Massachusetts tienen los montos promedio de donación más altos, mientras que Clarks Point, Swiftwater y North English son las ciudades con los promedios más elevados.
<img src="/Practica04/images/3.7.png">

#### 3.8 Montos Totales Donados por Estado
Se muestra la distribución del monto total donado por cada estado, permitiendo identificar geográficamente en dónde se concentra la mayor parte de la recaudación de DonorsChoose.
<img src="/Practica04/images/3.8.png">

#### 3.9 Donaciones de California a lo largo del tiempo
El número máximo de donaciones diarias en California se registró el 25 de enero de 2018 (casi 5,000 donaciones), seguido del 28 de noviembre de 2017 (4,699 donaciones).
<img src="/Practica04/images/3.9.png">

#### 4. Exploración de los Maestros
#### 4.1 Vista Rápida de los Datos de Maestros
Existen 402,900 maestros que han publicado al menos un proyecto en DonorsChoose desde 2002, siendo la gran mayoría mujeres.
<img src="/Practica04/images/4.1.png">

#### 4.2 Quiénes fueron los Primeros Maestros en DonorsChoose
Los primeros maestros se registraron el 17 de septiembre de 2002 (2 maestras ese día). En todo septiembre de 2002 se registraron 8 maestros, el primer grupo de la plataforma.
<img src="/Practica04/images/4.2.png">

#### 4.3 Crecimiento en el Número de Maestros a lo largo de los años
El crecimiento fue lento en los primeros cinco años, con una tendencia al alza desde 2008 y un aumento masivo entre 2012 y 2013. El número de nuevos maestros alcanzó su punto máximo en 2016 (80K) y bajó ligeramente en 2017 (75K).
<img src="/Practica04/images/4.3.png">

#### 4.4 Cuál es la distribución de los Prefijos de los Maestros
Se analiza la distribución de los prefijos (Mrs., Ms., Mr., Dr., etc.) utilizados por los maestros registrados, reflejando también la proporción de género entre ellos.
<img src="/Practica04/images/4.4.png">

#### 4.5 Serie Temporal de Maestros publicando sus primeros proyectos
El mayor número de primeros proyectos se registró el 13 de septiembre de 2015 (2,067 proyectos), observándose picos recurrentes cada agosto entre 2014 y 2017.
<img src="/Practica04/images/4.5.png">

#### 5. Exploración de las Escuelas
#### 5.1 Vista Rápida de los Datos de Escuelas
Se han publicado proyectos desde un total de 72,993 escuelas diferentes hasta abril de 2018.
<img src="/Practica04/images/5.1.png">

#### 5.2 Qué Tipo de Escuelas por Metrópoli publican proyectos (y los Estados y Ciudades Principales)
La mayoría de las escuelas se ubican en zonas suburbanas y urbanas. Nueva York, Houston y Chicago son las tres ciudades principales donde se concentran las escuelas.
<img src="/Practica04/images/5.2.png">

#### 5.3 Distribución del Porcentaje de Almuerzo Gratuito en las Escuelas
Se muestra cómo se distribuye el porcentaje de estudiantes que reciben almuerzo gratuito o a precio reducido entre las escuelas registradas, un indicador del nivel socioeconómico de cada institución.
<img src="/Practica04/images/5.3.png">

#### 5.4 Qué tipos de escuelas están registrados en mayoría
La mayoría de las escuelas son Primarias (~35K), muy por encima de las Secundarias (~12K), Intermedias (~9K) o Academias (~4K).
<img src="/Practica04/images/5.4.png">

#### 6. Exploración de los Recursos
Los datos de recursos incluyen los artículos solicitados en cada proyecto: nombre, cantidad, precio unitario y proveedor.
#### 6.1 Vista Rápida de los Recursos
Se han realizado un total de 7,210,448 solicitudes de recursos por parte de los maestros hasta abril de 2018.
<img src="/Practica04/images/6.1.png">

#### 6.2 Artículos más populares
##### 6.2.1 Artículos más solicitados de todos los tiempos
##### 6.2.2 Artículos solicitados en grandes cantidades
El Apple iPad Mini es el artículo más solicitado de todos los tiempos, presente en más de 30 mil proyectos, seguido de los viajes escolares con más de 20 mil proyectos. También destacan las particiones de privacidad, muebles y asientos blandos.
<img src="/Practica04/images/6.2.png">

#### 6.3 Artículos más Caros
Los parques infantiles inclusivos (como los diseñados para niños con discapacidad) son los artículos más caros, con casi USD 100,000, seguidos de estructuras comerciales Little Tikes y gimnasios telescópicos.
<img src="/Practica04/images/6.3.png">

#### 6.4 Proveedores Famosos en DonorsChoose
Amazon Business es el proveedor más solicitado, con 3.2 millones de solicitudes, seguido de Lakeshore Learning Materials y AKJ Education. MarkerBot tiene el costo promedio por proyecto más alto (USD 2,000), y Best Buy Education también destaca por su precio promedio elevado.
<img src="/Practica04/images/6.4.png">

#### 7. Exploración de los Proyectos
Los datos de proyectos incluyen el maestro y escuela asociados, título, tipo, categoría y costo, entre otros atributos.
#### 7.1 Vista Rápida de los Proyectos
Vista general de la estructura y primeras filas del dataset de proyectos, base para los análisis posteriores.
<img src="/Practica04/images/7.1.png">

#### 7.2 Cuáles son las Categorías, Subcategorías y Categorías de Recursos más frecuentes de los proyectos publicados
La categoría principal más común es Alfabetización y Lenguaje (más de 800K proyectos), seguida de Matemáticas y Ciencias. Alfabetización, Matemáticas y Escritura son las subcategorías más comunes; Tecnología Educativa, Rincones de Lectura y Escritorios/Almacenamiento son los recursos más solicitados.
<img src="/Practica04/images/7.2.png">

#### 7.3 Cuál es la distribución del Tipo de Proyecto y el Estado Actual del Proyecto
Predominan los proyectos liderados por maestros. Cerca del 75% de todos los proyectos se financian por completo, mientras que el 21% expira; a mayo de 2018 había alrededor de 42K proyectos activos.
<img src="/Practica04/images/7.3.png">

#### 7.4 En qué días se publicaron y financiaron el máximo de proyectos?
Los maestros publican principalmente al final de la semana (viernes 16%, sábado 16%, domingo 17%), mientras que los lunes concentran el mayor número de proyectos financiados y cerrados.
<img src="/Practica04/images/7.4.png">

#### 7.5 En qué Trimestres se publican y financian los proyectos
El tercer trimestre (julio-agosto-septiembre) concentra la mayor cantidad de proyectos publicados, mientras que el cuarto trimestre es cuando más proyectos se financian y cierran.
<img src="/Practica04/images/7.5.png">

#### 7.6 En qué meses se publicaron los proyectos
Dentro del tercer trimestre, septiembre es el mes con más proyectos publicados, seguido de agosto; junio registra el menor número.
<img src="/Practica04/images/7.6.png">

#### 7.7 En qué año se publicaron los proyectos
El número de proyectos ha crecido de forma constante en los últimos cinco años, con alrededor de 300K proyectos publicados en 2017.
<img src="/Practica04/images/7.7.png">

#### 7.8 En qué año y mes, el costo del proyecto es más alto
Septiembre de 2014 destaca por un alto volumen de proyectos con costo promedio elevado; en 2015, abril, mayo, septiembre y octubre también presentan costos altos.
<img src="/Practica04/images/7.8.png">

#### 7.9 En qué año y categoría de grado, el costo del proyecto es más alto
Para los Grados 6-8 y 9-12 los costos más altos se dieron en 2015; para los Grados 3-5 y PreK-2, en 2014.
<img src="/Practica04/images/7.9.png">

#### 7.10 Categorías de Grado y Categorías de Recursos que tienen los costos de proyecto más altos
Los viajes escolares se organizan principalmente para grados superiores (9-12), seguidos de 6-8 y 3-5, con PreK-2 muy por debajo. Los visitantes son otro recurso clave costoso en todos los grados.
<img src="/Practica04/images/7.10.png">

#### 7.11 Como varia el estado del proyecto por año
En promedio, cerca del 70% de los proyectos publicados cada año se financian por completo, con tendencia creciente salvo en 2016 (bajó 6% respecto al año anterior). 2017 y 2015 fueron los mejores años, con ~78% de proyectos financiados.
<img src="/Practica04/images/7.11.png">

#### 7.12 Por cuántos días permanecieron activos los proyectos
La mayoría de los proyectos se financian en menos de 3 días; unos 55,000 proyectos se financiaron en un solo día y 48,627 se cerraron el mismo día de su publicación. El proyecto más largo tardó 288 días ("Empty Bowls, Full Hearts", USD 1,982, Harrison Park Elementary School, Michigan).
<img src="/Practica04/images/7.12.png">

#### 7.13 Como varia la proporción de proyectos financiados vs no financiados por estado
Georgia, Carolina del Sur y Misisipi son los estados con menor porcentaje de proyectos expirados o no financiados.
<img src="/Practica04/images/7.13.png">

#### 7.14 Cual es el costo promedio del proyecto por tipo de metrópoli de la escuela y categoría de recursos solicitados
Los viajes y visitantes son siempre las categorías más costosas en todos los tipos de metrópoli. Los pueblos tienen el costo promedio más alto para equipos deportivos y de ejercicio.
<img src="/Practica04/images/7.14.png">

#### 7.15 Cual es el costo promedio del proyecto por tipo de metrópoli de la escuela y nivel de grado de los proyectos
Los Grados 9-12 tienen el costo promedio más alto entre todas las categorías de grado; las zonas suburbanas presentan los precios más altos y los pueblos los más bajos.
<img src="/Practica04/images/7.15.png">

#### 8. Procesamiento de Lenguaje Natural para la Creación de Perfiles de Proyectos
Se realiza un análisis de texto/NLP sobre los ensayos de los proyectos, enfocado en un subconjunto reciente (abril 2018), previa limpieza del texto (eliminación de stopwords y puntuación).
#### 8.2 Análisis de Bolsa de Palabras
##### 8.2.1 Cuales son las principales palabras y frases utilizadas por los maestros en los ensayos
Las palabras más frecuentes en los ensayos son "school", "learning", "classroom" y "reading"; entre los bigramas destacan "flexible seating" y "english language". Temas recurrentes incluyen desayuno y almuerzo gratis, aprendizaje del idioma inglés y desafíos enfrentados por los estudiantes.
<img src="/Practica04/images/8.2.png">

##### 8.2.2 Como varian las frases principales utilizadas por estado
En Texas destacan ensayos sobre estudiantes afectados por el huracán Harvey y opciones de asientos flexibles; en Iowa, sobre estudiantes de distintos orígenes y nacionalidades; en Nueva York, sobre educación especial y escuelas en zonas de pobreza; en Florida, sobre precios reducidos de desayuno y almuerzo.
<img src="/Practica04/images/8.2.2.png">

##### 8.2.3 "My Students Are " : Qué describen los maestros sobre sus estudiantes
Los maestros describen a sus estudiantes principalmente como "amazing", "awesome", "incredible" y "creative", además de "muy especiales" y "notables".
<img src="/Practica04/images/8.2.3.png">

##### 8.2.4 Segun lo descrito por los maestros, que necesitan los estudiantes
La necesidad más mencionada son las opciones de asientos flexibles, seguida de robots de programación y suministros escolares básicos. En tecnología destacan tabletas Amazon Fire, audífonos y el Osmo Genius Kit.
<img src="/Practica04/images/8.2.4.png">

##### 8.2.5 Título del Proyecto : Principales Palabras Utilizadas
Los títulos de los proyectos giran principalmente en torno a asientos flexibles, Chromebooks, lectura, aprendizaje, tecnología y libros.
<img src="/Practica04/images/8.2.5.png">

#### 9. Entendiendo y Comparando las Características Clave de los Proyectos
#### 9.1 Proyectos Expirados vs Proyectos Financiados
Los proyectos de PreK-2, en zonas urbanas y con costo menor a USD 500 tienen mayor porcentaje de éxito. Los ensayos con más de 250 palabras y los proyectos publicados en el cuarto trimestre (octubre-diciembre) también se financian más. Por el contrario, los proyectos con requerimientos tecnológicos costosos (iPads, Chromebooks) tienden a expirar más.
<img src="/Practica04/images/9.1.png">

#### 9.2 Proyectos con Duración de Financiación Corta vs Larga
Los proyectos financiados en un día o menos suelen ser de Grados 6-12, en zonas suburbanas, con costo menor a USD 500 y ensayos más extensos (>250 palabras). Los publicados en diciembre y septiembre tienden a tardar más en financiarse.
<img src="/Practica04/images/9.2.png">
<img src="/Practica04/images/9.3.1.png">

#### 9.3 Proyectos con Donante Único vs Múltiples Donantes
Los proyectos con un solo donante suelen ser de PreK-2, en zonas urbanas, de menor costo, con ensayos breves (<250 palabras) y relacionados con libros. Los proyectos con múltiples donantes corresponden más a grados superiores (3-12), zonas suburbanas/rurales, mayor costo (>USD 500) y están relacionados con tecnología y suministros.
<img src="/Practica04/images/9.3.2.png">
<img src="/Practica04/images/9.3.3.png">



### Notebook

[![Abrir notebook](https://github.com/DiegoMiguel04/ECBD-9A-IDGS-PRACTICAS-230260/blob/main/Practica04/Practica04_230260.ipynb)](practica04_230260.ipynb)

---

<center>

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&style=for-the-badge)
![Pandas](https://img.shields.io/badge/pandas-1.0%2B-0e76a8?logo=pandas&style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-1.18%2B-darkblue?logo=numpy&style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11%2B-4C9ACA?style=for-the-badge)

</center>
