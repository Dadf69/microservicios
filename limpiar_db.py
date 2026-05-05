from services.paises.conexion import mi_cursor, mi_db

# Limpiar registros de test
mi_cursor.execute("DELETE FROM paises WHERE idPais IN ('TE', 'T0', 'T1', 'T2', 'T01', 'T02', 'NE', 'PC', 'NEWTEST')")
mi_db.commit()

# Verificar
mi_cursor.execute("SELECT idPais FROM paises")
print('Registros restantes:', [r[0] for r in mi_cursor.fetchall()])
