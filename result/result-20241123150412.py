def query_all_doctors(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the SQL query to retrieve all doctors
        query = """
        SELECT DoctorID, FirstName, LastName, Specialty, PhoneNumber
        FROM Doctors
        """

        # Execute the query
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return the result as a list of dictionaries
        return [
            {
                "DoctorID": row.DoctorID,
                "FirstName": row.FirstName,
                "LastName": row.LastName,
                "Specialty": row.Specialty,
                "PhoneNumber": row.PhoneNumber
            }
            for row in result
        ]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"
doctors = query_all_doctors(connection_string)
for doctor in doctors:
    print(doctor)