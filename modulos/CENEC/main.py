from connect_db import initialize_sql


connection = initialize_sql()

if connection:
    try:
        cursor = connection.cursor()
        sql_query = """
        WITH PrePivot AS (
            SELECT m2.ruc, m2.cod_clave, CAST(m2.dato1 AS FLOAT) AS dato1
            FROM dbo_Modulo02_det_CCO AS m2
            INNER JOIN dbo_Capi_glosa AS cg
            ON m2.cod_clave = cg.GLOS_CODIGO
            WHERE cg.CAPI_CODIGO = '002'
            AND m2.ruc = '20100274206'
            AND m2.cod_clave = '006'
        )
        SELECT ruc, [006]
        FROM PrePivot
        PIVOT (
            SUM(dato1)
            FOR cod_clave IN ([006])
        ) AS pvt
        ORDER BY ruc ASC;
        """

        cursor.execute(sql_query)

        results = cursor.fetchall()

        for row in results:
            print(row)

    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()
else:
    print("No se pudo establecer la conexión a la base de datos.")
