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
| id_paciente | Identificador unico (ej. PBI-330A834E) |
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

Antes de generar el dataset completo se genero un primer conjunto de prueba de 15 registros (`ejemplo_15_registros.csv`), validado manualmente para confirmar que los rangos y la coherencia clinica fueran correctos, y despues se escalo el mismo proceso a los 5,000 registros finales.
