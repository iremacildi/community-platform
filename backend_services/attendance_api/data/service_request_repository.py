from data.db_manager import db
from sqlalchemy import and_

class ServiceRequestRepository(db.Model):
    __tablename__ = "servicerequest"
    id = db.Column(db.Integer, primary_key=True)
    serviceid = db.Column(db.Integer)
    userid = db.Column(db.Integer)
    providerid = db.Column(db.Integer)
    isapproved = db.Column(db.Boolean)
    isanswered = db.Column(db.Boolean)
    isactive = db.Column(db.Boolean)
    iscompleted = db.Column(db.Boolean)

    def __init__(self, serviceid, userid, providerid, isapproved, isanswered, isactive, iscompleted):
        self.serviceid = serviceid
        self.userid = userid
        self.providerid = providerid
        self.isapproved = isapproved
        self.isanswered = isanswered
        self.isactive = isactive
        self.iscompleted = iscompleted
    
    def add(self):
        db.session.add(self)
        db.session.commit()
        db.session.flush()

        return self

    def update(self):
        db.session.commit()
        db.session.flush()

        return self

    def delete(id):
        ServiceRequestRepository.query.filter_by(id=id).delete()
        db.session.commit()
    
    def getbyid(id):
        servicerequest = ServiceRequestRepository.query.filter_by(id=id).first()

        return servicerequest
    
    def getbyuserid(userid):
        servicerequests = ServiceRequestRepository.query.filter_by(userid=userid).all()

        return servicerequests

    def getbyserviceid(serviceid):
        servicerequests = ServiceRequestRepository.query.filter_by(serviceid=serviceid).all()

        return servicerequests
    
    def getbyproviderid(providerid):
        servicerequests = ServiceRequestRepository.query.filter_by(providerid=providerid).all()

        return servicerequests

    def diduserrequestbefore(userid, serviceid):
        events = ServiceRequestRepository.query.filter(and_(ServiceRequestRepository.userid==userid, ServiceRequestRepository.serviceid==serviceid)).all()

        return events