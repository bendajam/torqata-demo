from flask import Blueprint, jsonify, request
from app import models, schemas, login_required

person_schema = schemas.PersonDetailSchema()
persons_schema = schemas.PersonSchema(many=True)

actors = Blueprint('actors', __name__, url_prefix = '/api/actor')
directors = Blueprint('directors', __name__, url_prefix = '/api/director')

@actors.route('/list', methods=['GET'])
@login_required
def actors_list():
  page = request.args.get('page', 1, type=int)
  per_page = request.args.get('per_page', 50, type=int)

  results = models.Person.query.join(models.Person, models.Show.cast).paginate(page,per_page)
  return jsonify(
    {
      'result': persons_schema.dump(results.items),
      'page': page,
      'per_page': per_page,
      'total': results.total
    }
  )

@actors.route('/<int:actor_id>', methods=['GET'])
@login_required
def actors_detail(actor_id: int):
  actor = models.Person.query.join(models.Show, models.Person.cast).filter(models.Person.id == actor_id).first()
  return jsonify({'result': person_schema.dump(actor)})


@directors.route('/list', methods=['GET'])
@login_required
def director_list():
  page = request.args.get('page', 1, type=int)
  per_page = request.args.get('per_page', 50, type=int)

  results = models.Person.query.join(models.Person, models.Show.directors).paginate(page,per_page)
  return jsonify(
    {
      'result': persons_schema.dump(results.items),
      'page': page,
      'per_page': per_page,
      'total': results.total
    }
  )

@actors.route('/<int:actor_id>', methods=['GET'])
@login_required
def director_details(actor_id: int):
  director = models.Person.query.join(models.Person, models.Show.directors).filter(models.Person.id == actor_id).first()
  return jsonify({'result': person_schema.dump(director)})


