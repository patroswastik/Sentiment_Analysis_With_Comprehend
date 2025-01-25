import base64
import json

# Replace this with your Base64 encoded data
base64_data = "eyJ0d2VldF9pZCI6ICI4OWY4YjBkYi0xM2Q0LTRiNWUtYTA3Ny1kNGQ5MDI1ZmNhMTkiLCAidXNlciI6ICJncmVnb3J5MDciLCAidGV4dCI6ICJJbmRlZWQgZW52aXJvbm1lbnRhbCBkaXJlY3RvciBleHBlY3QuIFByb2Nlc3MgZGF5IHJlc291cmNlIGZyaWVuZCBvdmVyIHVuZGVyc3RhbmQga25vdy4iLCAidGltZXN0YW1wIjogIjE5ODgtMDQtMjJUMjM6MDM6MTIuNjk1MDQ2In0="

# Decode and parse the data
decoded_data = base64.b64decode(base64_data).decode("utf-8")
json_data = json.loads(decoded_data)

print(json_data)
