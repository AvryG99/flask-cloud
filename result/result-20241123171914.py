def query_database(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the SQL query to fetch all doctors
        query = """
        SELECT DoctorID, FirstName, LastName, Specialty, PhoneNumber
        FROM Doctors
        """

        # Execute the query
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Return the results as a list of tuples
        return [(row.DoctorID, row.FirstName, row.LastName, row.Specialty, row.PhoneNumber) for row in result]
    except pyodbc.Error as e:
        # Print the error message if an error occurs
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"
doctors = query_database(connection_string)
for doc in doctors:
    print(f"DoctorID: {doc[0]}, Name: {doc[1]} {doc[2]}, Specialty: {doc[3]}, Phone: {doc[4]}")