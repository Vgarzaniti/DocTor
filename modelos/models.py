from sqlalchemy import create_engine, Column, Integer, String, Boolean, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ObraSocial(Base):
    __tablename__ = 'obraSocial'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

class Dbt(Base):
    __tablename__ = 'dbt'
    id = Column(Integer, primary_key=True)
    tipo = Column(Integer, nullable=False)

class Cardiologico(Base):
    __tablename__ = 'cardiologico'
    id = Column(Integer, primary_key=True)
    arritmia = Column(Boolean, nullable=False)
    iam = Column(Boolean, nullable=False)
    marcapaso = Column(Boolean, nullable=False)
    stent = Column(Boolean, nullable=False)
    otro = Column(Text, nullable=False)

class Antecedentes(Base):
    __tablename__ = 'antecedentes'
    id = Column(Integer, primary_key=True)
    hta = Column(Boolean, nullable=False)
    idDbt = Column(Integer, ForeignKey('dbt.id'), nullable=False)
    dislipemia = Column(Boolean, nullable=False)
    hipotiroidismo = Column(Boolean, nullable=False)
    oncologico = Column(Text, nullable=False)
    cirugia = Column(Text, nullable=False)
    otros = Column(Text, nullable=False)
    idCardiologico = Column(Integer, ForeignKey('cardiologico.id'), nullable=False)

    dbt = relationship('Dbt', back_populates='antecedentes')
    cardiologico = relationship('Cardiologico', back_populates='antecedentes')

class Paciente(Base):
    __tablename__ = 'paciente'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    idObraSocial = Column(Integer, ForeignKey('obraSocial.id'), nullable=False)
    idAntecedentes = Column(Integer, ForeignKey('antecedentes.id'), nullable=False)

    obraSocial = relationship('ObraSocial', back_populates='pacientes')
    antecedentes = relationship('Antecedentes', back_populates='pacientes')

class Consulta(Base):
    __tablename__ = 'consulta'
    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    descripcion = Column(Text, nullable=False)
    idPaciente = Column(Integer, ForeignKey('paciente.id'), nullable=False)

    paciente = relationship('Paciente', back_populates='consultas')

class Extra(Base):
    __tablename__ = 'extra'
    id = Column(Integer, primary_key=True)
    nombreFarmaco = Column(Text, nullable=False)
    laboratorio = Column(Text, nullable=False)
    estudios = Column(Text, nullable=False)

class ConsultaXExtra(Base):
    __tablename__ = 'consultaXextra'
    id = Column(Integer, primary_key=True)
    idconsulta = Column(Integer, ForeignKey('consulta.id'), nullable=False)
    idextra = Column(Integer, ForeignKey('extra.id'), nullable=False)

    consulta = relationship('Consulta', back_populates='extras')
    extra = relationship('Extra', back_populates='consultas')

class PacienteXObraSocial(Base):
    __tablename__ = 'pacienteXobraSocial'
    id = Column(Integer, primary_key=True)
    numeroObraSocial = Column(Integer, nullable=False)
    idpaciente = Column(Integer, ForeignKey('paciente.id'), nullable=False)
    idobraSocial = Column(Integer, ForeignKey('obraSocial.id'), nullable=False)

    paciente = relationship('Paciente', back_populates='pacientesXObraSocial')
    obraSocial = relationship('ObraSocial', back_populates='pacientesXObraSocial')
