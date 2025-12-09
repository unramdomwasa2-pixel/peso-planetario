import streamlit as st

Luna = 0.165
Mercurio = 0.38
Venus = 0.90
Marte = 0.38
Jupiter = 2.53
Saturno = 1.06
Urano = 0.89
Neptuno = 1.14
Ceres = 0.028
Pluton = 0.063
Io = 0.18
Sol = 27.9

planetas = ["Luna", "Mercurio", "Venus", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno", "Ceres", "Pluton", "Io", "Sol"]

st.title("Calculadora de peso en otros planetas")

st.write("Ingrese un numero entero --OBLIGATORIO--")

peso = st.text_input("Escriba su peso:")
planeta = st.selectbox("Elija un planeta: ", ["Luna", "Mercurio", "Venus", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno", "Ceres", "Pluton", "Io", "Sol"])

if peso and planeta:
    peso = int(peso)

    if planeta == "Luna":
        st.write("Tu peso en Luna es: ", peso * Luna, "Kg")
    elif planeta == "Mercurio":
        st.write("Tu peso en Mercurio es: ", peso * Mercurio, "Kg")
    elif planeta == "Venus":
        st.write("Tu peso en Venus es: ", peso * Venus, "Kg")
    elif planeta == "Marte":
        st.write("Tu peso en Marte es: ", peso * Marte, "Kg")
    elif planeta == "Jupiter":
        st.write("Tu peso en Jupiter es: ", peso * Jupiter, "Kg")
    elif planeta == "Saturno":
        st.write("Tu peso en Saturno es: ", peso * Saturno, "Kg")
    elif planeta == "Urano":
        st.write("Tu peso en Urano es: ", peso * Urano, "Kg")
    elif planeta == "Neptuno":
        st.write("Tu peso en Neptuno es: ", peso * Neptuno, "Kg")
    elif planeta == "Ceres":
        st.write("Tu peso en Ceres es: ", peso * Ceres, "Kg")
    elif planeta == "Pluton":
        st.write("Tu peso en Pluton es: ", peso * Pluton, "Kg")
    elif planeta == "Io":
        st.write("Tu peso en Io es: ", peso * Io, "Kg")
    elif planeta == "Sol":
        st.write("Tu peso en el Sol es: ", peso * Sol, "Kg")
    else:
        st.error("Planeta no válido. Revisa la inicial.")