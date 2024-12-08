def query_database(connection_string):
    import pyodbc

    try:
        # Establish connection
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to find doctors who prescribed Metformin
        query = """
        SELECT DISTINCT d.FirstName, d.LastName
        FROM Medicines m
        JOIN PatientMedicines pm ON m.MedicineID = pm.MedicineID
        JOIN PatientDoctor pd ON pm.PatientID = pd.PatientID
        JOIN Doctors d ON pd.DoctorID = d.DoctorID
        WHERE m.MedicineName = 'Metformin'
        """

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        # Return a list of doctor names
        return [(row.FirstName, row.LastName) for row in result]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Define the connection string
connection_string = "driver={ODBC Driver 17 for SQL Server};server=MSI;database=EHR;Trusted_Connection=yes;"

# Execute the function
doctors_prescribing_metformin = query_database(connection_string)

# Print the results
for doctor in doctors_prescribing_metformin:
    print(f"Doctor: {doctor[0]} {doctor[1]}")