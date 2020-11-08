import pyodbc 


def connect_db(server='journal-mssql', port=1433, database='CompSciencePub', username='sa', password='mustafa1618'):
    """
    Create a new Database Connection
    """
    return pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};' +
                      ('SERVER={server},{port};' +
                       'DATABASE={database};' +
                       'UID={username};' +
                       'PWD={password}').format(
                        server=server,
                        port=port,
                        database=database,
                        username=username,
                        password=password)
                      )


def execute_query(query):
    """
    Execute Query to MSSQL Database
    ----------
    query : string
        The SQL statement will be executed
    
    """
    # Create DB Connection
    conn  = connect_db()
    cursor = conn.cursor()
    
    # Execute Query
    cursor.execute(query)

    # Get Columns from cursor
    columns = [column[0] for column in cursor.description]
    return map_cursor_to_dict(cursor, columns)


def map_cursor_to_dict(cursor, columns):
    """
    Map Cursor results to the dict
    """
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results

