import streamlit as st

# Page config
st.set_page_config(
    page_title="Thyroid Data Collection",
    layout="wide",
    page_icon="🧾",
    initial_sidebar_state="expanded"
)

# Sidebar
#st.sidebar.image("logo.jpg", use_container_width=True)
st.sidebar.title("Model A: Diagnosis")

# Title
st.title("Predictive Model for Thyroid Cancer Diagnosis")

# --- Input Form ---
st.header("Demographics")

cd1, cd2 = st.columns(2)
with cd1:
    age = st.number_input("Age (years)", min_value=0, max_value=120, step=1)
with cd2:
    gender_display = st.radio("Gender", ["Female", "Male"])
    gender = 0 if gender_display == "Female" else 1

# Imaging (USG)
st.header("Imaging (USG)")

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    usg_tirads = st.selectbox("TI-RADS Score", [1,2,3,4,5])
    usg_max_size_mm = st.number_input("Largest nodule size (mm)", min_value=0.0, step=0.1)
with c2:
    usg_composition = st.radio("Composition", ["Solid", "Mixed", "Cystic"])
    usg_calcifications_display = st.radio("Microcalcifications", ["Absent", "Present"])
    usg_calcifications = 0 if usg_calcifications_display == "Absent" else 1
with c3:
    usg_echogenicity = st.radio("Echogenicity", ["Hypo", "Iso", "Hyper"])
    usg_vascularity = st.radio("Vascularity", ["None", "Peripheral", "Intranodular"])
with c4:
    usg_shape_display = st.radio("Shape", ["Wider-than-tall", "Taller-than-wide"])
    usg_shape = 0 if usg_shape_display == "Wider-than-tall" else 1
    usg_extrathyroidal_display = st.radio("Signs of invasion", ["No", "Yes"])
    usg_extrathyroidal_extension = 0 if usg_extrathyroidal_display == "No" else 1
with c5:
    usg_margins_display = st.radio("Margins", ["Regular", "Irregular/Spiculated"])
    usg_margins = 0 if usg_margins_display == "Regular" else 1
    usg_lymph_nodes_display = st.radio("Suspicious lymph nodes", ["No", "Yes"])
    usg_suspicious_lymph_nodes = 0 if usg_lymph_nodes_display == "No" else 1

st.header("FNAC (Cytology)")

cf1, cf2, cf3, cf4 = st.columns(4)
with cf1:
    fnac_bethesda = st.selectbox("Bethesda category (I–VI as 1–6)", [1,2,3,4,5,6])
with cf2:
    fnac_nuclear_display = st.radio("Nuclear atypia", ["Absent", "Present"])
    fnac_nuclear_atypia = 0 if fnac_nuclear_display == "Absent" else 1
with cf3:
    fnac_colloid_display = st.radio("Colloid", ["Present", "Absent"])
    fnac_colloid = 0 if fnac_colloid_display == "Present" else 1
with cf4:
    fnac_cellularity = st.radio("Cellularity", ["Low", "Moderate", "High"])
    fnac_cellularity = {"Low":1, "Moderate":2, "High":3}[fnac_cellularity]

st.header("Hematology / Biochemical")

ch1, ch2, ch3, ch4 = st.columns(4)
with ch1:
    tsh = st.number_input("TSH (mIU/L)", min_value=0.0, step=0.1)
    calcitonin = st.number_input("Calcitonin (pg/mL)", min_value=0.0, step=0.1)
with ch2:
    cea = st.number_input("CEA (ng/mL)", min_value=0.0, step=0.1)
    tg = st.number_input("Thyroglobulin (ng/mL)", min_value=0.0, step=0.1)
with ch3:
    nlr = st.number_input("NLR (ratio)", min_value=0.0, step=0.1)
    plr = st.number_input("PLR (ratio)", min_value=0.0, step=0.1)
with ch4:
    tgab_display = st.radio("Anti-thyroglobulin antibodies", ["Negative", "Positive"])
    tgab = 0 if tgab_display == "Negative" else 1

# --- Submit Button ---
if st.button("Submit"):
    st.success("✅ Data submitted successfully!")
    st.write({
        "age": age,
        "gender": gender,
        "usg_tirads": usg_tirads,
        "usg_max_size_mm": usg_max_size_mm,
        "usg_composition": usg_composition,
        "usg_echogenicity": usg_echogenicity,
        "usg_shape": usg_shape,
        "usg_margins": usg_margins,
        "usg_calcifications": usg_calcifications,
        "usg_vascularity": usg_vascularity,
        "usg_extrathyroidal_extension": usg_extrathyroidal_extension,
        "usg_suspicious_lymph_nodes": usg_suspicious_lymph_nodes,
        "fnac_bethesda": fnac_bethesda,
        "fnac_nuclear_atypia": fnac_nuclear_atypia,
        "fnac_colloid": fnac_colloid,
        "fnac_cellularity": fnac_cellularity,
        "tsh": tsh,
        "calcitonin": calcitonin,
        "cea": cea,
        "tg": tg,
        "tgab": tgab,
        "nlr": nlr,
        "plr": plr
    })

# --- Footer ---
st.markdown(
    """
    <style>
    footer {visibility: hidden;}
    </style>
    <footer>
    <p style="text-align:center;">Developed by Ari Kustiawan</p>
    </footer>
    """,
    unsafe_allow_html=True,
)
