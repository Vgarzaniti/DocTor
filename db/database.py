from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos.models import Base  # Asegúrate de que models esté en la misma carpeta o importado correctamente

# URL de conexión a la base de datos en neon.tech
DATABASE_URL = "postgresql://Neon-Database_owner:npg_AeTMWEc40xQa@ep-calm-snow-a8t6p7jx-pooler.eastus2.azure.neon.tech/Neon-Database?sslmode=require"

# Crear la conexión con la base de datos
engine = create_engine(DATABASE_URL)

# Crear las tablas si no existen
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)

# Función que devuelve una nueva sesión
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
