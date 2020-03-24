from dataclasses import dataclass

import requests
from flask.views import MethodView
from flask import render_template, request


@dataclass
class Templates:
    one: str
    many: str


class Base(MethodView):
    def __init__(self, templates, api_url):
        self.api_url = api_url
        self.templates = templates

    @classmethod
    def register(cls, app, endpoint, url, templates, api_url):
        view_func = cls.as_view(endpoint, templates=templates, api_url=api_url)
        app.add_url_rule(url, view_func=view_func, methods=('GET', 'POST'))
        app.add_url_rule(f'{url}<int:id_>', view_func=view_func,
                         methods=('GET', 'PUT', 'DELETE'))

    def get(self, id_=None):
        if id_ is None:
            res = requests.get(self.api_url)
            return self._render_many(res)
        res = requests.get(f'{self.api_url}/{id_}')
        return self._render_one(res)

    def post(self):
        res = requests.post(self.api_url, data=request.form)
        return self.get()

    def put(self, id_):
        res = request.put(f'{self.api_url}/{id_}', data=request.form)
        return self.get()

    def delete(self, id_):
        res = request.delete(f'{self.api_url}/{id_}')
        return self._render_many(res)

    def _render_many(self, res):
        entities = res.json().get('data')
        return render_template(self.templates.many,
                               data=self._transform_many(entities))

    def _render_one(self, res):
        entity = res.json().get('data')
        return render_template(self.templates.one,
                               data=self._transform_one(entity))

    def _transform_many(self, entities):
        raise NotImplementedError

    def _transform_one(self, entity):
        raise NotImplementedError

