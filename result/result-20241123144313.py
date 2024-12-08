def query_database(connection_string):
    import pyodbc

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        query = """
        SELECT PatientID, FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber
        FROM Patients
        """

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        # Return a list of dictionaries containing patient information
        return [
            {
                'PatientID': row.PatientID,
                'FirstName': row.FirstName,
                'LastName': row.LastName,
                'DateOfBirth': row.DateOfBirth,
                'Gender': row.Gender,
                'Address': row.Address,
                'PhoneNumber': row.PhoneNumber
            }
            for row in result
        ]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = "driver=None;server=None;database=None;UID=None;PWD=None;"
patients = query_database(connection_string)
for patient in patients:
    print(patient)