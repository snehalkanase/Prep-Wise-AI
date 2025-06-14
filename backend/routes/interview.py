from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import uuid
from app import db
from models.interview import Interview
from ml.question_generator import generate_questions

interview_bp = Blueprint("interview", __name__)


@interview_bp.route("/", methods=["POST"])
@jwt_required()
def create_interview():
    user_id = get_jwt_identity()
    data = request.get_json()
    required_fields = ["role", "job_description", "experience", "num_questions"]
    missing = [field for field in required_fields if field not in data]

    if missing:
        return jsonify({"msg": f"Missing fields: {missing}"}), 400

    role = data.get("role")
    job_description = data.get("job_description")
    experience = data.get("experience")
    num_questions = data.get("num_questions")
    # Generate a unique alphanumeric interview ID
    interview_id = str(uuid.uuid4())
    interview = Interview(
        id=interview_id, 
        user_id=user_id,
        role=role,
        job_description=job_description,
        experience=experience,
        num_questions=num_questions,
    )
    db.session.add(interview)
    db.session.commit()

    return jsonify({"msg": "Interview created", "interview_id": interview.id}), 201


@interview_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_interviews():
    user_id = get_jwt_identity()
    interviews = Interview.query.filter_by(user_id=user_id).all()
    results = [
        {
            "id": i.id,
            "role": i.role,
            "job_description": i.job_description,
            "experience": i.experience,
            "created_at": i.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for i in interviews
    ]
    return jsonify(results), 200


@interview_bp.route("/<string:interview_id>", methods=["GET"])
@jwt_required()
def get_interview(interview_id):
    user_id = get_jwt_identity()
    interview = Interview.query.filter_by(id=interview_id, user_id=user_id).first()

    if not interview:
        return jsonify({"msg": "Interview not found"}), 404

    result = {
        "id": interview.id,
        "role": interview.role,
        "experience": interview.experience,
        "job_description": interview.job_description,
        "num_questions": interview.num_questions,
        "created_at": interview.created_at.strftime("%Y-%m-%d %H:%M:%S"),
    }

    return jsonify(result), 200


@interview_bp.route("/generate-questions/<string:interview_id>", methods=["GET"])
@jwt_required()
def generate_interview_questions(interview_id):
    user_id = get_jwt_identity()
    interview = Interview.query.filter_by(id=interview_id, user_id=user_id).first()

    if not interview:
        return jsonify({"msg": "Interview not found"}), 404

    questions = generate_questions(
        job_description_text=interview.job_description,
        role=interview.role,
        experience=interview.experience,
        num_questions=interview.num_questions
    )

    return jsonify({"questions": questions}), 200