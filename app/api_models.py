from flask_restx import fields

from .extensions import api


student_model = api.model("Student", {
    "id": fields.Integer,
    "user_name": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String,
    "password": fields.String
})

lecturer_model = api.model("Lecturer", {
    "id": fields.Integer,
    "user_name": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String,
    "password": fields.String
})

event_model = api.model("Event", {
    "id": fields.Integer,
    "title": fields.String,
    "venue": fields.String,
    "description": fields.String,
    "start_time": fields.String,
    "end_time": fields.String
})

student_input_model = api.model("StudentInput", {
    "user_name": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String,
    "password": fields.String
})

lecturer_input_model = api.model("LecturerInput", {
    "user_name": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String,
    "password": fields.String
})

event_input_model = api.model("EventInput", {
    "title": fields.String,
    "venue": fields.String,
    "description": fields.String,
    "start_time": fields.String,
    "end_time": fields.String
})