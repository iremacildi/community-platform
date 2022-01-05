from data.db_manager import db

class EventRepository(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(500))
    pictureurl = db.Column(db.String(120))
    location = db.Column(db.String(120))
    startdate = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    capacity = db.Column(db.Integer)
    organizeruserid = db.Column(db.Integer)
    isactive = db.Column(db.Boolean)

    def __init__(self, name, description, pictureurl, location, startdate, duration, capacity, organizeruserid, isactive):
        self.name = name
        self.description = description
        self.pictureurl = pictureurl
        self.location = location
        self.startdate = startdate
        self.duration = duration
        self.capacity = capacity
        self.organizeruserid = organizeruserid
        self.isactive = isactive
    
    def add(self):
        db.session.add(self)
        db.session.commit()
        db.session.flush()

        return self
    
    def get(organizeruserid):
        event = EventRepository.query.filter_by(organizeruserid=organizeruserid).first()

        return event