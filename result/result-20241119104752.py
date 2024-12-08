def query_database(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to find doctors who prescribed Metformin
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
        
        # Fetch all results
        result = cursor.fetchall()
        
        # Close the connection
        conn.close()

        # Process the results into a list of tuples
        return [(row.FirstName, row.LastName) for row in result]

    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Usage
connection_string = "driver={ODBC Driver 17 for SQL Server};server=MSI;database=EHR;Trusted_Connection=yes;"
doctors_prescribing_metformin = query_database(connection_string)

# Print results
for doctor in doctors_prescribing_metformin:
    print(f"Doctor: {doctor[0]} {doctor[1]}")