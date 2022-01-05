from flask import request, jsonify, make_response
from app import app
from data.service_request_repository import ServiceRequestRepository
from model.service_request_model import service_request_model
import json

@app.route("/")
def hello():
    resp = make_response(f'This is Attendance API. I am alive.', 200)
    resp.set_cookie('attendanceapi', 'attendance api is working.', httponly=True)
    return resp

@app.route('/servicerequest', methods=['PUT'])
def create_service():
    #authentication eklenecek 
    servicerequest = json.loads(request.data)
    userid = servicerequest["userid"]
    serviceid = servicerequest["serviceid"]

    servicerequestrepo = ServiceRequestRepository(serviceid, userid, 2, False, True)
    try:
        newservicerequest = servicerequestrepo.add()
        result = service_request_model.dump(newservicerequest)
        return jsonify({'issuccessful':'true', 'message':'Great! Your service request has been sent.'})
    except:
        return jsonify({'issuccessful':'false', 'message':'We couldn not send your request somehow. Sorry...'})