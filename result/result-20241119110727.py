def query_database(connection_string):
    import pyodbc

    try:
        # Connect to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the query to find doctors who prescribed Metformin
        query = """
        SELECT DISTINCT d.FirstName, d.LastName
        FROM Doctors d
        JOIN PatientDoctor pd ON d.DoctorID = pd.DoctorID
        JOIN PatientMedicines pm ON pd.PatientID = pm.PatientID
        JOIN Medicines m ON pm.MedicineID = m.MedicineID
        WHERE m.MedicineName = 'Metformin'
        """

        # Execute the query
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return the list of doctors
        return [(row.FirstName, row.LastName) for row in result]
    
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = 'driver={ODBC Driver 17 for SQL Server};server=MSI;database=EHR;Trusted_Connection=yes;'
doctors_prescribed_metformin = query_database(connection_string)
for doctor in doctors_prescribed_metformin:
    print(f"Doctor: {doctor[0]} {doctor[1]}")