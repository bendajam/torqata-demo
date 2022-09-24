from flask import Blueprint, jsonify, request
from sqlalchemy import text
from app import models, schemas

show_schema = schemas.ShowSchema()
shows_schema = schemas.ShowSchema(many=True)

shows = Blueprint('shows', __name__, url_prefix='/api/show')


@shows.route('/list', methods=['GET'])
def show_list():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 50, type=int)
    sort = request.args.get('sort', 'title', type=str)
    sort_dir = request.args.get('sort_dir', 'asc', type=str)

    results = models.Show.query.order_by(
        text(sort + " " + sort_dir)).paginate(page, per_page)
    return jsonify(
        {
            'result': shows_schema.dump(results.items),
            'page': page,
            'per_page': per_page,
            'total': results.total
        }
    )


@shows.route('/<int:show_id>', methods=['GET'])
def show_detail(show_id: int):
    show = models.Show.query.get(show_id)
    return jsonify({'result': show_schema.dump(show)})
