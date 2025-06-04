from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


# se importa información del archivo configuracion
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()


# Clase para la tabla 'reaccion' que une usuarios y publicaciones con una emoción
class Reaccion(Base):
    __tablename__ = 'reaccion'
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)  # Clave primaria y foránea
    publicacion_id = Column(Integer, ForeignKey('publicacion.id'), primary_key=True)  # Clave primaria y foránea
    tipo_emocion = Column(String(200), nullable=False)  # Tipo de emoción que puso el usuario

    # Relaciones para acceder fácilmente desde Reaccion a Usuario y Publicacion
    publicacion = relationship("Publicacion", back_populates="usuarios")
    usuario = relationship("Usuario", back_populates="reacciones")

    def __repr__(self):
        return (
            f"╔═══════════════════════════════════════════════\n"
            f"║   Usuario: {self.usuario.nombre}\n"
            f"║   Publicación: {self.publicacion.mensaje}\n"
            f"║   Emoción: {self.tipo_emocion}\n"
            f"╚═══════════════════════════════════════════════"
            )

# Clase para la tabla 'usuario'
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)  # ID único del usuario
    nombre = Column(String(200))  # Nombre del usuario

    # Relación con publicaciones, para saber que publicaciones creó
    publicaciones = relationship("Publicacion", back_populates="usuario")

    # Relación con Reaccion para saber en qué publicaciones reaccionó
    reacciones = relationship("Reaccion", back_populates="usuario")

    def __repr__(self):
        return (
            f"╔════════════════════════════\n"
            f"║   ID: {self.id}\n"
            f"║   Nombre: {self.nombre}\n"
            f"╚════════════════════════════"
        )

# Clase para la tabla 'publicacion'
class Publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)  # ID único de la publicación
    usuario_id = Column(Integer, ForeignKey('usuario.id'))  # El usuario que publicó
    mensaje = Column(String(200))  # El contenido de la publicación

    # Relación para saber que usuario creó la publicación
    usuario = relationship("Usuario", back_populates="publicaciones")

    # Relación con Reaccion para saber quiénes reaccionaron
    usuarios = relationship("Reaccion", back_populates="publicacion")

    def __repr__(self):
        return (
            f"╔══════════════════════════════════════════════════════\n"
            f"║   ID: {self.id}\n"
            f"║   Usuario: {self.usuario.nombre}\n"
            f"║   Mensaje: {self.mensaje}\n"
            f"╚══════════════════════════════════════════════════════"
        )

# Crea las tablas en la base de datos si no existen
Base.metadata.create_all(engine)

# ALISrj & cbhas