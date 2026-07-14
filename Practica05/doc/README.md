## Descripcion del dataset

`dataset_riesgo_infarto_puebla.csv` — dataset clinico sintetico, academico, no real, generado para entrenar modelos de clasificacion multiclase de riesgo de infarto cardiaco. Simula pacientes generales del estado de Puebla.

#### Ficha tecnica
- Registros: 5,000 pacientes
- Columnas: 33
- Formato: CSV, UTF-8 con BOM
- Valores nulos: presentes de forma intencional en columnas de laboratorio (4-8%), simulando estudios clinicos incompletos
- Variable objetivo: `riesgo_cardiovascular` (Bajo / Medio / Alto), calculada mediante un score ponderado de factores clinicos y de estilo de vida mas ruido aleatorio, para evitar relaciones perfectamente deterministas

---

#### Columnas

**Identificacion y administrativos**
| Columna | Descripcion |
|---|---|
| id_paciente | Identificador unico (ej. PUE-330A834E) |
| fecha_registro | Fecha de captura del registro |

**Demograficos, geograficos y socioeconomicos**
| Columna | Descripcion |
|---|---|
| edad | 18-95 anios |
| sexo | Femenino / Masculino |
| municipio | Municipio de Puebla (17 municipios, ponderados por poblacion) |
| zona | Urbana / Rural |
| nivel_socioeconomico | Bajo, Medio-bajo, Medio, Medio-alto, Alto |
| escolaridad | Sin escolaridad, Primaria, Secundaria, Preparatoria, Licenciatura, Posgrado |
| ocupacion | 12 categorias (comerciante, obrero, agricultor, etc.) |
| seguridad_social | IMSS, ISSSTE, IMSS-Bienestar, INSABI, Privado, Ninguna |

**Antropometricos y signos vitales**
| Columna | Descripcion |
|---|---|
| peso_kg | Peso en kg |
| estatura_cm | Estatura en cm |
| imc | Indice de masa corporal |
| imc_categoria | Bajo peso, Normal, Sobrepeso, Obesidad |
| presion_sistolica / presion_diastolica | mmHg |
| frecuencia_cardiaca | Latidos por minuto |
| saturacion_oxigeno | % SpO2 |

**Laboratorio clinico**
| Columna | Descripcion |
|---|---|
| glucosa_ayunas_mgdl | Glucosa en ayunas |
| colesterol_total_mgdl | Colesterol total |
| hdl_mgdl / ldl_mgdl | Colesterol HDL/LDL |
| trigliceridos_mgdl | Trigliceridos |

**Estilo de vida y factores de riesgo**
| Columna | Descripcion |
|---|---|
| actividad_fisica | Sedentario, Ligera, Moderada, Intensa |
| tabaquismo | No fumador, Ex-fumador, Ocasional, Habitual |
| consumo_alcohol | Nulo, Ocasional, Moderado, Frecuente |
| dieta_calidad | Mala, Regular, Buena |
| horas_sueno | Horas de sueno promedio |
| estres_percibido_1_10 | Escala subjetiva 1-10 |
| antecedentes_familiares_cardiacos | 0/1 |
| diabetes_diagnosticada | 0/1 |
| hipertension_diagnosticada | 0/1 |

**Variable objetivo**
| Columna | Descripcion |
|---|---|
| riesgo_cardiovascular | Bajo / Medio / Alto |

---

#### Simulacion

**Metodologia utilizada para la generacion del dataset:**
El dataset se genero mediante un script de Python (`numpy` + `pandas`) que construye cada variable a partir de distribuciones estadisticas realistas (normales, categoricas ponderadas) y encadena dependencias clinicas logicas entre variables — por ejemplo, la presion arterial y la glucosa aumentan con la edad, el IMC y los diagnosticos previos de hipertension/diabetes. La variable objetivo `riesgo_cardiovascular` se calcula con un score ponderado de los principales factores de riesgo (edad, IMC, presion, diabetes, hipertension, antecedentes familiares, tabaquismo, sedentarismo, dieta, alcohol y colesterol) mas un termino de ruido aleatorio, de forma que la relacion entre variables y clase no sea perfectamente determinista y existan casos atipicos.

El archivo `ejemplo_15_registros.csv` **no es un conjunto generado por separado**: es una muestra aleatoria de 15 registros extraida directamente del dataset final de 5,000 pacientes (con semilla fija, `random_state=230317`, para que sea reproducible), tomada unicamente de filas sin valores nulos. Su proposito es servir como referencia rapida y legible de la estructura y coherencia clinica del dataset completo, sin necesidad de abrir el CSV de 5,000 registros.

---

#### Muestra de los 15 registros de ejemplo

A continuacion se muestran, agrupados por categoria, los 15 registros reales contenidos en `ejemplo_15_registros.csv`:

**Identificacion y demograficos**

| id_paciente   | fecha_registro   |   edad | sexo      | municipio           | zona   | nivel_socioeconomico   | escolaridad     | ocupacion                   | seguridad_social   |
|:--------------|:-----------------|-------:|:----------|:--------------------|:-------|:-----------------------|:----------------|:----------------------------|:-------------------|
| PUE-A7610EE4  | 2024-06-04       |     48 | Femenino  | Amozoc              | rural  | Medio-bajo             | Secundaria      | Obrero/a                    | INSABI             |
| PUE-ACC70F58  | 2024-10-12       |     31 | Femenino  | Acatlan             | rural  | Medio-bajo             | Preparatoria    | Comerciante                 | Privado            |
| PUE-402BD380  | 2025-11-25       |     35 | Femenino  | Zacatlan            | urbana | Medio-bajo             | Secundaria      | Empleado/a de oficina       | ISSSTE             |
| PUE-D6B0B37D  | 2025-09-25       |     66 | Masculino | Puebla              | urbana | Medio-bajo             | Sin escolaridad | Profesionista independiente | IMSS               |
| PUE-58A3CCCA  | 2024-12-10       |     40 | Masculino | Atlixco             | urbana | Medio                  | Secundaria      | Jubilado/a                  | Privado            |
| PUE-D0B5CDC4  | 2025-08-27       |     43 | Femenino  | Puebla              | rural  | Medio-bajo             | Primaria        | Jubilado/a                  | IMSS-Bienestar     |
| PUE-CF299DA7  | 2024-07-24       |     50 | Masculino | Izucar de Matamoros | rural  | Medio                  | Secundaria      | Desempleado/a               | IMSS               |
| PUE-34FC05C6  | 2025-08-26       |     79 | Masculino | Tehuacan            | rural  | Alto                   | Licenciatura    | Chofer/transportista        | Privado            |
| PUE-36B569F9  | 2025-09-09       |     45 | Masculino | Acatlan             | urbana | Medio-alto             | Secundaria      | Artesano/a                  | ISSSTE             |
| PUE-FF6867F1  | 2025-03-03       |     51 | Masculino | Atlixco             | urbana | Bajo                   | Preparatoria    | Agricultor/a                | IMSS-Bienestar     |
| PUE-2D1FCE79  | 2024-11-26       |     89 | Femenino  | Atlixco             | urbana | Bajo                   | Preparatoria    | Chofer/transportista        | INSABI             |
| PUE-7205284C  | 2025-01-21       |     67 | Femenino  | Atlixco             | rural  | Medio-alto             | Primaria        | Estudiante                  | IMSS               |
| PUE-FC402E89  | 2024-08-05       |     38 | Masculino | Amozoc              | urbana | Alto                   | Secundaria      | Artesano/a                  | IMSS               |
| PUE-F082097D  | 2025-01-23       |     45 | Femenino  | Amozoc              | urbana | Alto                   | Sin escolaridad | Chofer/transportista        | IMSS               |
| PUE-C371A34D  | 2024-06-12       |     75 | Masculino | San Pedro Cholula   | rural  | Medio                  | Preparatoria    | Chofer/transportista        | IMSS-Bienestar     |


**Antropometricos y signos vitales**

| id_paciente   |   peso_kg |   estatura_cm |   imc | imc_categoria   |   presion_sistolica |   presion_diastolica |   frecuencia_cardiaca |   saturacion_oxigeno |
|:--------------|----------:|--------------:|------:|:----------------|--------------------:|---------------------:|----------------------:|---------------------:|
| PUE-A7610EE4  |      50.2 |         162.1 |  19.1 | Normal          |                 104 |                   62 |                    68 |                 96.3 |
| PUE-ACC70F58  |      65.4 |         159.6 |  25.7 | Sobrepeso       |                 112 |                   72 |                    83 |                 97.5 |
| PUE-402BD380  |      82.4 |         163.1 |  30.9 | Obesidad        |                 106 |                   55 |                    67 |                 97.9 |
| PUE-D6B0B37D  |      91.8 |         182   |  27.7 | Sobrepeso       |                 115 |                   74 |                    87 |                 95.7 |
| PUE-58A3CCCA  |      89.7 |         166.6 |  32.3 | Obesidad        |                 108 |                   68 |                    65 |                 97.5 |
| PUE-D0B5CDC4  |      79.6 |         156.3 |  32.6 | Obesidad        |                 117 |                   67 |                    77 |                 96.6 |
| PUE-CF299DA7  |      57.7 |         164.3 |  21.4 | Normal          |                 111 |                   77 |                    77 |                 97.8 |
| PUE-34FC05C6  |      66.4 |         155.3 |  27.5 | Sobrepeso       |                 135 |                   85 |                    61 |                 96.7 |
| PUE-36B569F9  |      41.4 |         166.1 |  15   | Bajo peso       |                  94 |                   63 |                    73 |                 96.5 |
| PUE-FF6867F1  |      81.4 |         168.8 |  28.6 | Sobrepeso       |                  87 |                   64 |                    73 |                 98.4 |
| PUE-2D1FCE79  |      54.3 |         162.4 |  20.6 | Normal          |                 126 |                   78 |                   105 |                 96.4 |
| PUE-7205284C  |      60   |         158.1 |  24   | Normal          |                 129 |                   80 |                    85 |                 99.1 |
| PUE-FC402E89  |      94.4 |         164.3 |  35   | Obesidad        |                  99 |                   72 |                    90 |                 96.5 |
| PUE-F082097D  |      75.8 |         157.1 |  30.7 | Obesidad        |                 115 |                   78 |                    75 |                 94   |
| PUE-C371A34D  |      78.3 |         167.5 |  27.9 | Sobrepeso       |                 130 |                   85 |                    66 |                 96.9 |


**Laboratorio clinico**

| id_paciente   |   glucosa_ayunas_mgdl |   colesterol_total_mgdl |   hdl_mgdl |   ldl_mgdl |   trigliceridos_mgdl |
|:--------------|----------------------:|------------------------:|-----------:|-----------:|---------------------:|
| PUE-A7610EE4  |                    86 |                   145   |       47.6 |       75.7 |                 88.4 |
| PUE-ACC70F58  |                   104 |                   176.1 |       53.6 |       78.4 |                256.7 |
| PUE-402BD380  |                    85 |                   238   |       54.8 |      185.9 |                200.6 |
| PUE-D6B0B37D  |                   110 |                   264.3 |       34.6 |      194.1 |                230.5 |
| PUE-58A3CCCA  |                   104 |                   206.7 |       31.4 |      143   |                151.2 |
| PUE-D0B5CDC4  |                    91 |                   245.8 |       30.8 |      166.7 |                122.7 |
| PUE-CF299DA7  |                   157 |                   125   |       39.8 |       43.5 |                282.8 |
| PUE-34FC05C6  |                   147 |                   195.4 |       46.7 |      124.4 |                173.5 |
| PUE-36B569F9  |                    73 |                   241.7 |       57.3 |      161.2 |                140.1 |
| PUE-FF6867F1  |                    94 |                   165.6 |       49.6 |      118.5 |                119.2 |
| PUE-2D1FCE79  |                   101 |                   248.2 |       54.3 |      150.8 |                182.4 |
| PUE-7205284C  |                   117 |                   257.2 |       26.8 |      214.5 |                 94.7 |
| PUE-FC402E89  |                    99 |                   160.2 |       52.7 |       84.6 |                146.1 |
| PUE-F082097D  |                   106 |                   200.9 |       34.1 |      159   |                123.4 |
| PUE-C371A34D  |                   193 |                   200   |       32.8 |      137   |                220   |


**Estilo de vida y factores de riesgo**

| id_paciente   | actividad_fisica   | tabaquismo   | consumo_alcohol   | dieta_calidad   |   horas_sueno |   estres_percibido_1_10 |   antecedentes_familiares_cardiacos |   diabetes_diagnosticada |   hipertension_diagnosticada |
|:--------------|:-------------------|:-------------|:------------------|:----------------|--------------:|------------------------:|------------------------------------:|-------------------------:|-----------------------------:|
| PUE-A7610EE4  | Moderada           | No fumador   | Ocasional         | Mala            |           5.2 |                      10 |                                   1 |                        0 |                            0 |
| PUE-ACC70F58  | Ligera             | Habitual     | Moderado          | Regular         |           5.7 |                       9 |                                   0 |                        0 |                            1 |
| PUE-402BD380  | Sedentario         | No fumador   | Nulo              | Buena           |           6.6 |                       2 |                                   0 |                        0 |                            0 |
| PUE-D6B0B37D  | Sedentario         | Ocasional    | Moderado          | Regular         |           4.6 |                       8 |                                   0 |                        0 |                            0 |
| PUE-58A3CCCA  | Moderada           | No fumador   | Nulo              | Buena           |           5.4 |                       1 |                                   0 |                        0 |                            0 |
| PUE-D0B5CDC4  | Sedentario         | Ex-fumador   | Ocasional         | Regular         |           7.1 |                       3 |                                   0 |                        0 |                            0 |
| PUE-CF299DA7  | Moderada           | No fumador   | Moderado          | Mala            |           4.8 |                       5 |                                   0 |                        1 |                            1 |
| PUE-34FC05C6  | Intensa            | No fumador   | Ocasional         | Buena           |           7.8 |                       3 |                                   1 |                        1 |                            1 |
| PUE-36B569F9  | Ligera             | Ex-fumador   | Nulo              | Regular         |           7.1 |                       3 |                                   0 |                        0 |                            0 |
| PUE-FF6867F1  | Ligera             | Habitual     | Frecuente         | Regular         |           4.6 |                       1 |                                   0 |                        0 |                            0 |
| PUE-2D1FCE79  | Intensa            | Ex-fumador   | Ocasional         | Buena           |           7.8 |                       3 |                                   0 |                        0 |                            1 |
| PUE-7205284C  | Moderada           | Habitual     | Nulo              | Mala            |           5   |                       9 |                                   0 |                        0 |                            0 |
| PUE-FC402E89  | Moderada           | No fumador   | Moderado          | Regular         |           5.5 |                       1 |                                   1 |                        0 |                            0 |
| PUE-F082097D  | Intensa            | No fumador   | Ocasional         | Regular         |           5.9 |                       5 |                                   1 |                        0 |                            1 |
| PUE-C371A34D  | Sedentario         | Ex-fumador   | Nulo              | Buena           |           7.6 |                       3 |                                   0 |                        1 |                            0 |


**Variable objetivo**

| id_paciente   | riesgo_cardiovascular   |
|:--------------|:------------------------|
| PUE-A7610EE4  | Bajo                    |
| PUE-ACC70F58  | Medio                   |
| PUE-402BD380  | Medio                   |
| PUE-D6B0B37D  | Medio                   |
| PUE-58A3CCCA  | Bajo                    |
| PUE-D0B5CDC4  | Medio                   |
| PUE-CF299DA7  | Medio                   |
| PUE-34FC05C6  | Alto                    |
| PUE-36B569F9  | Bajo                    |
| PUE-FF6867F1  | Medio                   |
| PUE-2D1FCE79  | Medio                   |
| PUE-7205284C  | Medio                   |
| PUE-FC402E89  | Bajo                    |
| PUE-F082097D  | Medio                   |
| PUE-C371A34D  | Alto                    |

