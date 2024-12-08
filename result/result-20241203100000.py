def query_database(connection_string):
    import pyodbc

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to get all diagnoses
        query = """
        SELECT DiagnosisCode, DiagnosisDescription
        FROM Diagnoses
        """

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        return [(row.DiagnosisCode, row.DiagnosisDescription) for row in result]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Connection string
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"

# Fetch and print all diagnoses
diagnoses = query_database(connection_string)
for diagnosis in diagnoses:
    print(diagnosis)