def query_doctors_prescribing_metformin(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to find doctors who prescribed Metformin
        query = """
        SELECT DISTINCT doc.FirstName, doc.LastName
        FROM Doctors doc
        JOIN PatientDoctor pd ON doc.DoctorID = pd.DoctorID
        JOIN PatientMedicines pm ON pd.PatientID = pm.PatientID
        JOIN Medicines m ON pm.MedicineID = m.MedicineID
        WHERE m.MedicineName = 'Metformin'
        """

        # Execute the query
        cursor.execute(query)

        # Fetch all results
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return a formatted list of tuples with doctor names
        return [(row.FirstName, row.LastName) for row in result]

    except pyodbc.Error as e:
        # Handle any errors in the connection or query
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = 'driver={ODBC Driver 17 for SQL Server};server=MSI;database=EHR;Trusted_Connection=yes;'
doctors = query_doctors_prescribing_metformin(connection_string)
for doctor in doctors:
    print(f"Dr. {doctor[0]} {doctor[1]}")