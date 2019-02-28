from flask import Flask, jsonify, request
from pixel_strip import createStrip
from led import imageLoop, drawData, runDemo, updatePixel
from render import motion
from pixel_rain import start_rain, end_rain


application = Flask(__name__, static_folder='script')
application.config['SECRET_KEY'] = 'top-secret!'

STRIP = createStrip()

# Response Dict
def request_ok(response_dict, success=True):
    response_dict.update({
        'success': success
    })
    resp = jsonify(**response_dict)
    resp.status_code = 200
    return resp

@application.route('/image_cycle', methods=['GET', 'POST'])
def image_cycle():
    imageLoop(STRIP)
    return request_ok({ 'message': 'Started Displaying Images.'})



@application.route('/set_pixel_box', methods=['POST'])
def set_pixel_box():
    json = request.get_json()
    img_data = None if 'img_data' not in json else json['img_data']
    drawData(STRIP,img_data)
    return request_ok({ 'message': 'Image Set'})

@application.route('/pixel_update', methods=['POST'])
def pixel_update():
    json = request.get_json()
    img_data = None if 'img_data' not in json else json['img_data']
    updatePixel(STRIP,img_data)
    return request_ok({ 'message': 'Pixel Updated'})

# Status Checkin


# Rain
@application.route('/rain_start', methods=['GET', 'POST'])
def rain_start():
    start_rain(STRIP)
    return request_ok({ 'message': 'Rain Complete'})

@application.route('/rain_stop', methods=['GET', 'POST'])
def rain_stop():
    end_rain()
    return request_ok({ 'message': 'Rain Stopped.'})

@application.route('/rain_toggle', methods=['GET', 'POST'])
def rain_stop():
    end_rain()
    return request_ok({ 'message': 'Rain Stopped.'})




@application.route('/ping', methods=['GET', 'POST'])
def ping():
    return request_ok({ 'message': 'P0NG!'})

@application.route('/test', methods=['GET', 'POST'])
def test():
    motion(STRIP)
    return request_ok({ 'message': 'Welcome to Amiblight\'s moblie API.'})
    
if __name__ == '__main__':
    application.run(debug=True,use_reloader=True, host='0.0.0.0', port=8080)
