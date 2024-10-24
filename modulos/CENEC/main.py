from connect_db import initialize_sql
import pandas as pd
import cronometro

start_time, fin_ejecucion, hilo_cronometro = cronometro.iniciar_cronometro()
connection = initialize_sql()

if connection:
    try:
        codigo = '003'
        cursor = connection.cursor()

        get_table = f"""
			select distinct Tabla from dbo_Capitulo WHERE CAPI_CODIGON='{codigo}'
		"""
        cursor.execute(get_table)
        tablaDB = cursor.fetchone()[0]


        sql_getCodClaves = f"""
            SELECT DISTINCT GLOS_CODIGO FROM dbo_Capi_glosa
            WHERE CAPI_CODIGO = '{codigo}'
        """
        cursor.execute(sql_getCodClaves)
        results = cursor.fetchall()
        cod_claves = '[' + '],['.join([row[0] for row in results]) + ']'

        sql_query = f"""
            WITH PrePivot AS (
            SELECT m2.ruc,e.razon_social, m2.cod_clave, CAST(m2.dato1 AS FLOAT) AS dato1
            FROM dbo_{tablaDB} AS m2
            INNER JOIN dbo_Capi_glosa AS cg
            ON m2.cod_clave = cg.GLOS_CODIGO
            INNER JOIN CPI.dbo.empresa AS e
            ON m2.ruc = e.id
            
            )
            SELECT ruc, razon_social, {cod_claves}
            FROM PrePivot
            PIVOT (
                SUM(dato1)
                FOR cod_clave IN ({cod_claves})
            ) AS pvt
            ORDER BY ruc ASC;
        """

        cursor.execute(sql_query)
        resultss = cursor.fetchall()

        pd.set_option('future.no_silent_downcasting', True)
        df = pd.DataFrame(resultss).fillna(0).infer_objects().transpose()
        df.to_excel('D:/excel_salida/prueba.xlsx', index=False, engine='openpyxl')


    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
    finally:
        cursor.close()
        connection.close()
        cronometro.detener_cronometro(start_time, fin_ejecucion, hilo_cronometro)
else:
    print("No se pudo establecer la conexión a la base de datos.")
# WHERE cg.CAPI_CODIGO = '{codigo}' and m2.ruc='20100274206' and (m2.cod_clave ='007' or m2.cod_clave ='006')