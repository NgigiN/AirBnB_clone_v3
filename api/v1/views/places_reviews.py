#!/usr/bin/python3
'''Contains the place_values view for the API.'''

from flask import jsonify, request
from werkzeug.exceptions import NotFound, MethodNotAllowed, BadRequest

from api.v1.views import app_views
from models import storage, storage_t
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'])
@app_views.route('/reviews/<review_id>', methods=['GET', 'DELETE', 'PUT'])
def handle_reviews(place_id=None, review_id=None):
    '''
    The method handler for the reviews endpoint.
    '''
    handlers = {
        'GET': get_reviews,
        'DELETE': remove_review,
        'POST': add_review,
        'PUT': update_review,
    }
    if request.method in handlers:
        return handlers[request.method](place_id, review_id)
    else:
        raise MethodNotAllowed(list(handlers.keys()))


def get_reviews(place_id=None, review_id=None):
    '''Gets the review with the given id or all reviews in
    the place with the given id.
    '''
    if place_id:
        place = storage.get(Place, place_id)
        if place:
            reviews = list(map(lambda x: x.to_dict(), place.reviews))
            return jsonify(reviews)
    elif review_id:
        review = storage.get(Review, review_id)
        if review:
            return jsonify(review.to_dict())
    raise NotFound()


def remove_review(place_id=None, review_id=None):
    '''Removes a review with the given id.
    '''
    if review_id:
        review = storage.get(Review, review_id)
        if review:
            storage.delete(review)
            return jsonify({}), 200
    raise NotFound()


def add_review(place_id=None, review_id=None):
    '''Adds a review to the place with the given id.
    '''
    if place_id:
        place = storage.get(Place, place_id)
        if place:
            data = request.get_json()
            if data:
                if 'user_id' in data:
                    user = storage.get(User, data['user_id'])
                    if user:
                        if 'text' in data:
                            review = Review(**data)
                            review.place_id = place_id
                            review.save()
                            return jsonify(review.to_dict()), 201
                        else:
                            raise BadRequest('Missing text')
                    else:
                        raise NotFound()
                else:
                    raise BadRequest('Missing user_id')
            else:
                raise BadRequest('Not a JSON')
    raise NotFound()


def update_review(place_id=None, review_id=None):
    '''Updates a review with the given id.
    '''
    if review_id:
        review = storage.get(Review, review_id)
        if review:
            data = request.get_json()
            if data:
                for key, value in data.items():
                    if key not in ['id', 'user_id', 'place_id', 'created_at',
                                   'updated_at']:
                        setattr(review, key, value)
                review.save()
                return jsonify(review.to_dict()), 200
            else:
                raise BadRequest('Not a JSON')
    raise NotFound()
