import pyodbc
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the connection details for the SQL database
server = '<server_name>'
database = '<database_name>'
username = '<username>'
password = '<password>'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Define the credentials for the Google Sheet API
scope = ['https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('<path_to_key_file>', scope)
client = gspread.authorize(creds)

# Define the SQL query
query = '<your_query_here>'

# Execute the query and fetch the results
with pyodbc.connect(connection_string) as conn:
    with conn.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

# Push the results to a Google Sheet
sheet = client.open('<sheet_name>').sheet1
#sheet.clear() # Clear existing data
sheet.insert_rows(rows) # Insert the new data
