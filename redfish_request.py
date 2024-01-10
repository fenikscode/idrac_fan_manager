import requests

# This data must be set specificly for user use
IP = "192.168.10.219"
USERNAME = "root"
PASSWORD = "#ostatni_walc"

def make_query():
    # This variable is getting data from server using RedFish protocol
    QUERY = requests.get(
        f"https://{IP}/redfish/v1/Chassis/System.Embedded.1/Thermal",
        verify=False,
        auth=(USERNAME, PASSWORD))
    
    # Query convertion to proper json format
    SERVER_QUERY = QUERY.json()
    RESPOND = []
    
    # This loop create and add specific entrys for later use
    for FAN_DATA in SERVER_QUERY['Fans']:
        RESPOND.append((FAN_DATA['Name'], FAN_DATA['Reading']))
    
    return RESPOND