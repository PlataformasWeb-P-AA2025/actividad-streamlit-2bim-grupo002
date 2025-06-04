# streamlit_explorar.py

import streamlit as st
from db import get_session

# Importa las clases que definiste en clases.py
from clases import *


st.set_page_config(page_title="Explorador de objetos SQLAlchemy", layout="wide")


def listar_usuarios():
    """
    Muestra todos los usuarios y, en un expander, más detalles.
    """
    st.header("Usuarios")
    session = get_session()
    usuarios = session.query(Usuario).all()


    if not usuarios:
        st.info("No hay registros en 'Usuario'.")
        session.close()
        return

    # Para cada Departamento, mostramos un expander que contiene su lista de cursos
    for u in usuarios:
        with st.expander(f"ID {u.id} → {u.nombre}", expanded=False):
            # Mostrar atributos básicos
            st.write(f"**ID:** {u.id}")
            st.write(f"**Nombre:** {u.nombre}")

            # Si el departamento tiene cursos relacionados, listarlos
            if u.publicaciones:
                st.write("**Publicaciones asociadas:**")
                # Usamos st.table para mostrar una tabla sencilla con el id, título e instructor
                filas = []
                for p in u.publicaciones:
                    filas.append({
                        "Publicación ID": p.id,
                        "Mensaje": p.mensaje,
                    })
                st.table(filas)
            else:
                st.write("_No hay publicaciones asociadas a este usuario._")
    session.close()

def listar_publicaciones():
    """
    Muestra todos los instructores y, dentro de cada expander, sus cursos.
    """
    st.header("Publicaciones")
    session = get_session()
    publicaciones = session.query(Publicacion).all()


    if not publicaciones:
        st.info("No hay registros en 'Publicaciones'.")
        session.close()
        return

    for p in publicaciones:
        with st.expander(f"ID {p.id} → {p.mensaje[0:25]}...", expanded=False):
            st.write(f"**Creador:** {p.usuario.nombre}")
            st.write(f"**ID:** {p.id}")
            st.write(f"**Mensaje:** {p.mensaje}")
    session.close()

def listar_reacciones():
    st.header("Reacciones")
    session = get_session()
    usuarios = session.query(Usuario).all()


    if not usuarios:
        st.info("No hay registros en 'Usuario'.")
        session.close()
        return

    # Para cada Departamento, mostramos un expander que contiene su lista de cursos
    for u in usuarios:
        with st.expander(f"ID {u.id} → {u.nombre}", expanded=False):
            # Mostrar atributos básicos
            st.write(f"**ID:** {u.id}")
            st.write(f"**Nombre:** {u.nombre}")

            # Si el departamento tiene cursos relacionados, listarlos
            if u.publicaciones:
                st.write("**Publicaciones asociadas:**")
                # Usamos st.table para mostrar una tabla sencilla con el id, título e instructor
                filas = []
                for p in u.publicaciones:
                    filas.append({
                        "Publicación ID": p.id,
                        "Mensaje": p.mensaje,
                    })
                st.table(filas)
            else:
                st.write("_No hay publicaciones asociadas a este usuario._")
    session.close()

def main():
    st.title("Explorador de objetos SQLAlchemy en Streamlit")

    entidad = st.sidebar.selectbox(
        "Elija la entidad que desea explorar:",
        (
            "Usuario",
            "Publicación",
            "Reacción",
        ),
    )

    if entidad == "Usuario":
        listar_usuarios()
    elif entidad == "Publicación":
        listar_publicaciones()
    elif entidad == "Curso":
        pass
        # listar_cursos()
    elif entidad == "Estudiante":
        pass
        # listar_estudiantes()
    elif entidad == "Inscripción":
        pass
        # listar_inscripciones()
    elif entidad == "Tarea":
        pass
        # listar_tareas()
    elif entidad == "Entrega":
        pass
        # listar_entregas()


if __name__ == "__main__":
    main()
