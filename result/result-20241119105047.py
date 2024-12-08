def get_doctors_prescribed_metformin(connection_string):
    import pyodbc

    try:
        # Connect to the SQL Server database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the SQL query
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
        
        # Return the results
        return [(row.FirstName, row.LastName) for row in result]
    
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Provide the connection string
connection_string = "driver={ODBC Driver 17 for SQL Server};server=MSI;database=EHR;Trusted_Connection=yes;"

# Call the function and print the results
doctors = get_doctors_prescribed_metformin(connection_string)
for first_name, last_name in doctors:
    print(f"Doctor: {first_name} {last_name}")