from flask import Flask, request
import urllib
# import databse
app = Flask(__name__)


def check_data_correctness(cell_id,
                           signal_strenght,
                           phone_gps_lat,
                           phone_gps_lng):
    # for now no cellID parameters
    # signal strenght parameters - values have to be corrected
    if signal_strenght >= -100 and signal_strenght <= 100:
        pass
    else:
        return False
    # phone_gps_lat parameters
    if phone_gps_lat >= -180 and signal_strenght <= 180:
        pass
    else:
        return False
    # phone_gps_lng parameters
    if phone_gps_lat >= -90 and signal_strenght <= 90:
        pass
    else:
        return False
    return True


@app.route('/api/post_message', methods=['POST'])
def post_message():
    print("Request: ", request.json)
    cell_id = request.json["cellid"]
    signal_strenght = request.json["dataArray"][0]["signal_Strength"]
    phone_gps_lat = request.json["dataArray"][0]["location"]["lati"]
    phone_gps_lng = request.json["dataArray"][0]["location"]["long"]
    print("CellID: ", cell_id)
    print("Signal strenght: ", signal_strenght)
    print("Phone GPS Lat: ", phone_gps_lat)
    print("Phone GPS Lng: ", phone_gps_lng)
    check_data_correctness(cell_id,
                           signal_strenght,
                           phone_gps_lat,
                           phone_gps_lng)
    # execute database handler
    # databse.handler(request.json)
    return "Post processed"


@app.route('/api/get_message', methods=['GET'])
def get_message():
    return "df"
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
