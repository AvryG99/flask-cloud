def query_database(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
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
        
        # Close the connection
        conn.close()

        # Return the results as a list of tuples
        return [(row.DiagnosisCode, row.DiagnosisDescription) for row in result]
    except pyodbc.Error as e:
        # Print an error message if a database error occurs
        print("Error executing query: ", e)
        return []

# Connection string for the database
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"

# Call the function and store the results
diagnoses = query_database(connection_string)

# Print the results
for diagnosis in diagnoses:
    print(diagnosis)