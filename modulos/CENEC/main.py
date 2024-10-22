from connect_db import initialize_sql

connection = initialize_sql()

if connection:
    try:
        cursor = connection.cursor()

        # Obtener los códigos claves
        sql_getCodClaves = """
            SELECT DISTINCT GLOS_CODIGO FROM dbo_Capi_glosa
            WHERE CAPI_CODIGO = '002'
        """
        cursor.execute(sql_getCodClaves)
        results = cursor.fetchall()

        # Verificar si se obtuvieron resultados
        if results:
            cod_claves = '[' + '],['.join([row[0] for row in results]) + ']'
        else:
            print("No se encontraron códigos clave.")
            cod_claves = ''  # Asegúrate de manejar este caso

        # Construir la consulta SQL
        sql_query = f"""
            WITH PrePivot AS (
            SELECT m2.ruc,e.razon_social, m2.cod_clave, CAST(m2.dato1 AS FLOAT) AS dato1
            FROM dbo_Modulo02_det_CCO AS m2
            INNER JOIN dbo_Capi_glosa AS cg
            ON m2.cod_clave = cg.GLOS_CODIGO
            INNER JOIN CPI.dbo.empresa AS e
            ON m2.ruc = e.id
            WHERE cg.CAPI_CODIGO = '002'
            )
            SELECT ruc, razon_social, {cod_claves}
            FROM PrePivot
            PIVOT (
                SUM(dato1)
                FOR cod_clave IN ({cod_claves})
            ) AS pvt
            ORDER BY ruc ASC;
        """

        # Ejecutar la consulta
        cursor.execute(sql_query)
        resultss = cursor.fetchall()

        # Mostrar los resultados
        for row in resultss:
            print(row)

    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
    finally:
        cursor.close()
        connection.close()
else:
    print("No se pudo establecer la conexión a la base de datos.")
