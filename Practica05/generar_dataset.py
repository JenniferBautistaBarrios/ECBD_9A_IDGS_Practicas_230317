import numpy as np
import pandas as pd
import uuid
from datetime import datetime, timedelta

rng = np.random.default_rng(230317)  # semilla propia (matricula) -> dataset propio y distinto
N = 5000

# ---------- Catalogos (17 municipios, incluye Xicotepec de Juarez) ----------
municipios = ["Puebla", "Tehuacan", "San Martin Texmelucan", "Atlixco", "San Pedro Cholula",
              "San Andres Cholula", "Amozoc", "Huauchinango", "Zacatlan", "Teziutlan",
              "Izucar de Matamoros", "Cuetzalan", "Chignahuapan", "Acatlan", "Tepeaca",
              "Xicotepec de Juarez", "Zacapoaxtla"]
pesos_municipio = np.array([0.27, 0.09, 0.06, 0.06, 0.07, 0.06, 0.05, 0.05, 0.03, 0.04,
                             0.04, 0.03, 0.03, 0.03, 0.02, 0.05, 0.02])
pesos_municipio = pesos_municipio / pesos_municipio.sum()

ocupaciones = ["Comerciante", "Obrero/a", "Agricultor/a", "Ama de casa", "Empleado/a de oficina",
               "Chofer/transportista", "Docente", "Profesionista independiente", "Estudiante",
               "Jubilado/a", "Artesano/a", "Desempleado/a"]

niveles_socio = ["Bajo", "Medio-bajo", "Medio", "Medio-alto", "Alto"]
seguridad_social = ["IMSS", "ISSSTE", "IMSS-Bienestar", "INSABI", "Privado", "Ninguna"]
act_fisica_cats = ["Sedentario", "Ligera", "Moderada", "Intensa"]
tabaquismo_cats = ["No fumador", "Ex-fumador", "Ocasional", "Habitual"]
alcohol_cats = ["Nulo", "Ocasional", "Moderado", "Frecuente"]
dieta_cats = ["Mala", "Regular", "Buena"]
escolaridad_cats = ["Sin escolaridad", "Primaria", "Secundaria", "Preparatoria", "Licenciatura", "Posgrado"]

def id_paciente():
    return f"PBI-{uuid.uuid4().hex[:8].upper()}"

def fecha_registro():
    inicio = datetime(2024, 3, 1)
    dias = rng.integers(0, 700)
    return (inicio + timedelta(days=int(dias))).strftime("%Y-%m-%d")

# ---------- Variables demograficas y antropometricas ----------
edad = rng.integers(18, 96, N)
sexo = rng.choice(["Femenino", "Masculino"], N)
municipio = rng.choice(municipios, N, p=pesos_municipio)
zona = rng.choice(["urbana", "rural"], N, p=[0.64, 0.36])
nivel_socio = rng.choice(niveles_socio, N, p=[0.22, 0.27, 0.27, 0.16, 0.08])
ocupacion = rng.choice(ocupaciones, N)
seg_social = rng.choice(seguridad_social, N, p=[0.40, 0.11, 0.20, 0.07, 0.14, 0.08])
escolaridad = rng.choice(escolaridad_cats, N, p=[0.06, 0.24, 0.28, 0.22, 0.16, 0.04])

estatura_cm = np.where(sexo == "Femenino",
                        rng.normal(157, 6.8, N),
                        rng.normal(169, 6.8, N))
estatura_cm = np.clip(estatura_cm, 140, 200)

imc_base = np.clip(rng.normal(27.5, 5.2, N), 15, 55)
peso_kg = imc_base * (estatura_cm / 100) ** 2
peso_kg = np.clip(peso_kg, 35, 180)
imc = peso_kg / (estatura_cm / 100) ** 2

def clasifica_imc(v):
    if v < 18.5:
        return "Bajo peso"
    elif v < 25:
        return "Normal"
    elif v < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"
imc_categoria = np.array([clasifica_imc(v) for v in imc])

actividad_fisica = rng.choice(act_fisica_cats, N, p=[0.34, 0.27, 0.27, 0.12])
tabaquismo = rng.choice(tabaquismo_cats, N, p=[0.53, 0.19, 0.16, 0.12])
consumo_alcohol = rng.choice(alcohol_cats, N, p=[0.34, 0.36, 0.22, 0.08])
dieta_calidad = rng.choice(dieta_cats, N, p=[0.28, 0.46, 0.26])
horas_sueno = np.clip(rng.normal(6.6, 1.3, N), 3, 11).round(1)
estres_percibido = np.clip(rng.integers(1, 11, N), 1, 10)

antecedentes_fam = rng.choice([0, 1], N, p=[0.66, 0.34])
diabetes_dx = rng.choice([0, 1], N, p=[0.84, 0.16])
hipertension_dx = rng.choice([0, 1], N, p=[0.76, 0.24])

# ---------- Signos vitales y laboratorio, correlacionados con edad/IMC/diagnosticos ----------
presion_sistolica = (96 + (edad - 18) * 0.36 + (imc - 25) * 0.85 +
                      hipertension_dx * 17 + rng.normal(0, 9, N))
presion_sistolica = np.clip(presion_sistolica, 85, 220).round().astype(int)

presion_diastolica = (61 + (edad - 18) * 0.16 + (imc - 25) * 0.42 +
                       hipertension_dx * 9 + rng.normal(0, 6, N))
presion_diastolica = np.clip(presion_diastolica, 55, 130).round().astype(int)

frecuencia_cardiaca = np.clip(rng.normal(76, 11, N) + (imc - 25) * 0.28, 45, 140).round().astype(int)
saturacion_oxigeno = np.clip(rng.normal(97, 1.5, N), 88, 100).round(1)

glucosa = (86 + (edad - 18) * 0.24 + diabetes_dx * 56 + (imc - 25) * 0.85 + rng.normal(0, 12, N))
glucosa = np.clip(glucosa, 60, 300).round().astype(int)

colesterol_total = np.clip(rng.normal(192, 34, N) + (edad - 18) * 0.28 + (imc - 25) * 0.58, 100, 350).round(1)
hdl = np.clip(rng.normal(47, 12, N) - (imc - 25) * 0.32, 20, 100).round(1)
ldl = np.clip(colesterol_total - hdl - rng.normal(30, 15, N), 40, 250).round(1)
trigliceridos = np.clip(rng.normal(152, 58, N) + (imc - 25) * 2.1, 40, 500).round(1)

# ---------- Score de riesgo ponderado + ruido aleatorio ----------
score = (
    (edad - 18) / 77 * 24 +
    (imc - 15) / 40 * 14 +
    (presion_sistolica - 85) / 135 * 16 +
    hipertension_dx * 12 +
    diabetes_dx * 12 +
    antecedentes_fam * 9 +
    (tabaquismo == "Habitual") * 8 +
    (tabaquismo == "Ocasional") * 3 +
    (actividad_fisica == "Sedentario") * 6 +
    (dieta_calidad == "Mala") * 5 +
    (consumo_alcohol == "Frecuente") * 4 +
    (colesterol_total - 100) / 250 * 8 +
    rng.normal(0, 9, N)
)
score = np.clip(score, 0, 100)
riesgo = pd.cut(score, bins=[-1, 31, 59, 101], labels=["Bajo", "Medio", "Alto"])

# ---------- Ensamble del DataFrame ----------
df = pd.DataFrame({
    "id_paciente": [id_paciente() for _ in range(N)],
    "fecha_registro": [fecha_registro() for _ in range(N)],
    "edad": edad,
    "sexo": sexo,
    "municipio": municipio,
    "zona": zona,
    "nivel_socioeconomico": nivel_socio,
    "escolaridad": escolaridad,
    "ocupacion": ocupacion,
    "seguridad_social": seg_social,
    "peso_kg": peso_kg.round(1),
    "estatura_cm": estatura_cm.round(1),
    "imc": imc.round(1),
    "imc_categoria": imc_categoria,
    "presion_sistolica": presion_sistolica,
    "presion_diastolica": presion_diastolica,
    "frecuencia_cardiaca": frecuencia_cardiaca,
    "saturacion_oxigeno": saturacion_oxigeno,
    "glucosa_ayunas_mgdl": glucosa,
    "colesterol_total_mgdl": colesterol_total,
    "hdl_mgdl": hdl,
    "ldl_mgdl": ldl,
    "trigliceridos_mgdl": trigliceridos,
    "actividad_fisica": actividad_fisica,
    "tabaquismo": tabaquismo,
    "consumo_alcohol": consumo_alcohol,
    "dieta_calidad": dieta_calidad,
    "horas_sueno": horas_sueno,
    "estres_percibido_1_10": estres_percibido,
    "antecedentes_familiares_cardiacos": antecedentes_fam,
    "diabetes_diagnosticada": diabetes_dx,
    "hipertension_diagnosticada": hipertension_dx,
    "riesgo_cardiovascular": riesgo.astype(str),
})

# ---------- Nulos intencionales en columnas de laboratorio (4-8%) ----------
lab_cols = ["saturacion_oxigeno", "colesterol_total_mgdl", "hdl_mgdl", "ldl_mgdl", "trigliceridos_mgdl"]
for col in lab_cols:
    frac = rng.uniform(0.04, 0.08)
    idx = rng.choice(df.index, size=int(frac * N), replace=False)
    df.loc[idx, col] = np.nan

df.to_csv("datasets/dataset_riesgo_infarto_puebla.csv", index=False, encoding="utf-8-sig", lineterminator="\r\n")

# 15 registros de ejemplo (sin nulos, representativos) para doc/
ejemplo = df.dropna().sample(15, random_state=230317).reset_index(drop=True)
ejemplo.to_csv("doc/ejemplo_15_registros.csv", index=False, encoding="utf-8-sig", lineterminator="\r\n")

print(df.shape)
print(df.isnull().mean().round(3)[df.isnull().mean() > 0])
print(df["riesgo_cardiovascular"].value_counts())
