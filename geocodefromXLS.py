import pyexcel
import googlemaps
import json

def readData():
    fileName = 'C:\Users\hp\Desktop\pincodes.xlsx'
    my_dict = pyexcel.get_dict(file_name=fileName, name_columns_by_row=0)
    return my_dict

my_dict = readData()

gmaps = googlemaps.Client(key='AIzaSyBwFdXk2eoGJ8wCwtrOdgPeJvwt46k1GyQ')
gplace = googlemaps.Client(key='AIzaSyBZfI_k3gnQSYjB8ujC0HWRBtWuF7Ija4E')
type = raw_input("Enter type of search (e.g: for IT companies, type could be \"ITCompanies\"):")
query = raw_input("Enter query (e.g: for IT companies, query could be \"IT\"):")
radius = int(raw_input("Enter distance in km:"))
radius = radius * 1000

for pincode in my_dict['Pincodes']:
    geocode_result = gmaps.geocode(address=pincode)

    address = json.dumps(geocode_result)
    print "Address is : %s" % geocode_result[0]["formatted_address"]
    latiLongi = geocode_result[0]['geometry']['location']
    getResult = gplace.places(location=latiLongi, radius=radius, type=type, query=query)
    result = json.dumps(getResult)
    print result