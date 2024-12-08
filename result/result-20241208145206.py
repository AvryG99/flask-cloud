def get_john_doe_status(connection_string):
    import pyodbc

    try:
        # Establish database connection
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to fetch detailed information about John Doe
        query = """
        SELECT 
            p.FirstName, p.LastName, p.DateOfBirth, p.Gender, p.Address, p.PhoneNumber,
            d.DiagnosisDescription,
            m.MedicineName, pm.Dosage AS MedicineDosage, pm.PrescriptionDate,
            doc.FirstName AS DoctorFirstName, doc.LastName AS DoctorLastName, doc.Specialty
        FROM Patients p
        LEFT JOIN PatientDiagnoses pd ON p.PatientID = pd.PatientID
        LEFT JOIN Diagnoses d ON pd.DiagnosisID = d.DiagnosisID
        LEFT JOIN PatientMedicines pm ON p.PatientID = pm.PatientID
        LEFT JOIN Medicines m ON pm.MedicineID = m.MedicineID
        LEFT JOIN PatientDoctor pd2 ON p.PatientID = pd2.PatientID
        LEFT JOIN Doctors doc ON pd2.DoctorID = doc.DoctorID
        WHERE p.FirstName = 'John' AND p.LastName = 'Doe'
        """

        # Execute the query
        cursor.execute(query)
        results = cursor.fetchall()
        
        # Close the database connection
        conn.close()

        # Process and return the results
        detailed_status = []
        for row in results:
            detailed_status.append({
                'FirstName': row.FirstName,
                'LastName': row.LastName,
                'DateOfBirth': row.DateOfBirth,
                'Gender': row.Gender,
                'Address': row.Address,
                'PhoneNumber': row.PhoneNumber,
                'DiagnosisDescription': row.DiagnosisDescription,
                'MedicineName': row.MedicineName,
                'MedicineDosage': row.MedicineDosage,
                'PrescriptionDate': row.PrescriptionDate,
                'DoctorFirstName': row.DoctorFirstName,
                'DoctorLastName': row.DoctorLastName,
                'DoctorSpecialty': row.Specialty
            })

        return detailed_status

    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Define the connection string
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"

# Get John Doe's status
john_doe_status = get_john_doe_status(connection_string)

# Print the status details
for status in john_doe_status:
    print(status)