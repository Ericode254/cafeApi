from flask_restx import Resource, Namespace

from .api_models import student_model, lecturer_model, event_model, student_input_model, lecturer_input_model, event_input_model
from .models import Student, Lecturer, Event
from .extensions import db

ns = Namespace("api")


@ns.route("/students")
class StudentListApi(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()

    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    def post(self):
        student = Student(user_name=ns.payload["user_name"], 
                          first_name=ns.payload["first_name"], 
                          last_name=ns.payload["last_name"],
                          email=ns.payload["email"],
                          password=ns.payload["password"])
        db.session.add(student)
        db.session.commit()
        return student, 201


@ns.route("/students/<string:user>")
class StudentApi(Resource):
    @ns.marshal_with(student_model)
    def get(self, user):
        student = Student.query.filter_by(user_name=user).first()

        return student, 200


@ns.route("/lecturers")
class LecturerListApi(Resource):
    @ns.marshal_list_with(lecturer_model)
    def get(self):
        return Lecturer.query.all()

    @ns.expect(lecturer_input_model)
    @ns.marshal_with(lecturer_model)
    def post(self):
        lecturer = Lecturer(user_name=ns.payload["user_name"], 
                           first_name=ns.payload["first_name"], 
                           last_name=ns.payload["last_name"],
                           email=ns.payload["email"],
                           password=ns.payload["password"])
        db.session.add(lecturer)
        db.session.commit()
        return lecturer, 201


@ns.route("/lecturers/<string:user>")
class LecturerApi(Resource):
    @ns.marshal_with(lecturer_model)
    def get(self, user):
        lecturer = Lecturer.query.filter_by(user_name=user).first()

        return lecturer


@ns.route("/events")
class EventListApi(Resource):
    @ns.marshal_list_with(event_model)
    def get(self):
        return Event.query.all()

    @ns.expect(event_input_model)
    @ns.marshal_with(event_model)
    def post(self):
        event = Event(title=ns.payload["title"], 
                      venue=ns.payload["venue"], 
                      description=ns.payload["description"],
                      start_time=ns.payload["start_time"],
                      end_time=ns.payload["end_time"])
        db.session.add(event)
        db.session.commit()
        return event, 201


@ns.route("/events/<int:time>")
class EventApi(Resource):
    def delete(self, time):
        deleted_events = Event.query.filter(Event.end_time < time)
        db.session.delete(deleted_events)
        db.session.commit()
        return {}, 204


@ns.route("/events/<string:email>")
class EventApi(Resource):
    def delete(self, email):
        delete_event = Event.query.filter_by(email="email").first();
        db.session.delete(delete_event)
        db.session.commit()
        return {}, 204