def query_database(connection_string):
    import pyodbc

    try:
        # Establish connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to fetch all diagnoses of all patients
        query = """
        SELECT DISTINCT d.DiagnosisCode, d.DiagnosisDescription
        FROM Diagnoses d
        JOIN PatientDiagnoses pd ON d.DiagnosisID = pd.DiagnosisID
        """

        # Execute the query
        cursor.execute(query)

        # Fetch all results
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return the results as a list of tuples
        return [(row.DiagnosisCode, row.DiagnosisDescription) for row in result]

    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Example usage:
connection_string = "driver={ODBC Driver 17 for SQL Server};server=None;database=None;Trusted_Connection=yes;"
diagnoses = query_database(connection_string)
for diagnosis in diagnoses:
    print("Diagnosis Code:", diagnosis[0], "Description:", diagnosis[1])