from services.paises.conexion import mi_cursor, mi_db

# Limpiar registros de test
mi_cursor.execute("DELETE FROM paises WHERE idPais LIKE 'T%' OR idPais LIKE 'N%' OR idPais LIKE 'Z%' OR idPais LIKE 'Y%'")
mi_db.commit()

# Verificar
mi_cursor.execute("SELECT idPais, nombre FROM paises")
resultados = mi_cursor.fetchall()
print("Registros restantes:")
for r in resultados:
    print(f"  {r[0]}: {r[1]}")