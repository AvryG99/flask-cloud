def query_all_diagnoses(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the query to retrieve all diagnoses
        query = """
        SELECT DiagnosisID, DiagnosisCode, DiagnosisDescription
        FROM Diagnoses
        """

        # Execute the query
        cursor.execute(query)

        # Fetch all results
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return the results as a list of tuples
        return [(row.DiagnosisID, row.DiagnosisCode, row.DiagnosisDescription) for row in result]

    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Usage example
if __name__ == "__main__":
    connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"
    diagnoses = query_all_diagnoses(connection_string)
    for diagnosis in diagnoses:
        print(diagnosis)