from flask import Blueprint, redirect, url_for
from flask_restful import Api
from app.api.resources.articles import ArticleApi

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

@api_bp.route('/')
def api_redirect():
    return redirect(url_for('index'))

api.add_resource(ArticleApi, '/article/<int:article_id>', '/article', '/article/<int:article_id>/delete', '/articles')