def query_database(connection_string):
    import pyodbc

    try:
        # Establish the connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL Query to get the doctors who prescribed Metformin
        query = """
        SELECT DISTINCT d.FirstName, d.LastName, d.Specialty, d.PhoneNumber
        FROM Doctors d
        JOIN PatientDoctor pd ON d.DoctorID = pd.DoctorID
        JOIN PatientMedicines pm ON pd.PatientID = pm.PatientID
        JOIN Medicines m ON pm.MedicineID = m.MedicineID
        WHERE m.MedicineName = 'Metformin'
        """

        # Execute the query
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        # Format the result
        return [(row.FirstName, row.LastName, row.Specialty, row.PhoneNumber) for row in result]

    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Connection string provided in the question
connection_string = "driver={ODBC Driver 17 for SQL Server};server=MSI;database=EHR;Trusted_Connection=yes;"

# Call the function and output the results
doctors_who_prescribed_metformin = query_database(connection_string)
for doctor in doctors_who_prescribed_metformin:
    print(f"Doctor: {doctor[0]} {doctor[1]}, Specialty: {doctor[2]}, Phone: {doctor[3]}")