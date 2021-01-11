from flask_restful import Resource, reqparse
from app.models import Article, ArticleSchema
from flask import jsonify

parser = reqparse.RequestParser()

class ArticleApi(Resource):
    def get(self, article_id):
        article = Article.query.filter_by(id=article_id).first()
        if article:
            article_schema = ArticleSchema(many=False)
            return article_schema.jsonify(article)
        else:
            return 404
    
    def put(self):
        parser.add_argument('name', type=str)
        parser.add_argument('year_posted', type=str)
        parser.add_argument('count_of_pages', type=int)
        parser.add_argument('author', type=str)
        parser.add_argument('note', type=str)
        parser.add_argument('type_of_art', type=str)
        args = parser.parse_args(strict=True)

        article = Article(args['name'], args['year_posted'], args['count_of_pages'], args['author'], args['note'], args['type_of_art'])
        article.save()
        return 200
    
    def post(self):
        articles = Article.query.all()
        article_schema = ArticleSchema(many=True)
        
        return article_schema.jsonify(articles)
    
    def delete(self, article_id):
        article = Article.query.get(article_id)
        if article: 
            article.delete()
            return 200
        else:
            return 404