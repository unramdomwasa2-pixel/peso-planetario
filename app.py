import streamlit as st

st.markdown("""
    <style>
    div[data-baseweb="select"] > div, ul[role="listbox"], li[role="option"] {
        background-color: #1a3a5a !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<style>hr {border-color: #7CFC00 !important;}</style>', unsafe_allow_html=True)

st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        background-color: #1a3a5a !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<style>.stApp {background-size: 100% 100% !important; background-attachment: scroll !important;}</style>', unsafe_allow_html=True)

st.markdown('<style>* {font-family: serif !important; color: #FFFFFF !important;}</style>', unsafe_allow_html=True)

st.markdown("""
    <style>
    * {font-family: "Georgia", serif !important;}
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {
        top: -40px;
    }
    </style>
    """, unsafe_allow_html=True)

fondo = "https://i.pinimg.com/originals/35/97/6a/35976a472e0ae3152b39b080760909db.jpg"

st.markdown(f"""
<style>
.stApp {{
    background: url("{fondo}");
    background-size: cover;
}}
</style>
""", unsafe_allow_html=True)

espacio, title = st.columns([1, 4])
with title:
    st.title("Inversiones el criollo")

st.divider()

opc = st.selectbox("Menu", ["Platos", "bebidas", "postres"])

st.divider()

col1, desc1, desc2, col3 = st.columns(4)
with col1:
    if opc == "Platos":

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

        st.divider()

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

        st.divider()

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

with col3:
    if opc == "Platos":
        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

        st.divider()

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

        st.divider()

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")


beb1, dc1, dc2, beb3 = st.columns(4)

with beb1:
    if opc == "bebidas":

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

        st.divider()

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

        st.divider()

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

with beb3:
    if opc == "bebidas":

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

        st.divider()

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

        st.divider()

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")


pos1, d1, d2, pos3 = st.columns(4)

with pos1:
    if opc == "postres":
        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

        st.divider()

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

        st.divider()

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

with pos3:
    if opc == "postres":
        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

        st.divider()

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")

        st.divider()

        st.subheader("Pabellon criollo")
        st.write("Delicioso plato de arroz, caraotas, platano, huevo y carne mechada")
        st.image("https://mojo.generalmills.com/api/public/content/rvFCh00FckGn5UlOJh153Q_gmi_hi_res_jpeg.jpeg?v=452d812a&t=16e3ce250f244648bef28c5949fb99ff", width=100)
        st.subheader("9,99$")
