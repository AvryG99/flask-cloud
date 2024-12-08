def get_all_diagnoses(connection_string):
    import pyodbc

    try:
        # Establish a connection to the SQL Server database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the SQL query to retrieve all diagnoses
        query = """
        SELECT DiagnosisCode, DiagnosisDescription
        FROM Diagnoses
        """

        # Execute the query
        cursor.execute(query)

        # Fetch all results from the executed query
        result = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Return the results as a list of tuples
        return [(row.DiagnosisCode, row.DiagnosisDescription) for row in result]

    except pyodbc.Error as e:
        # Print error message if any exception occurs
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"
diagnoses = get_all_diagnoses(connection_string)
for diagnosis in diagnoses:
    print(diagnosis)