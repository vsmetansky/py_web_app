import os

import requests
from flask import render_template
from flask.views import MethodView

API_BASE_URL = os.environ['API_BASE_URL']


class Departments(MethodView):
    def get(self):
        res = requests.get(f'http://{API_BASE_URL}/departments')
        deps = res.json().get('data')
        return render_template('departments.html',
                               data=self._get_deps_data(deps))

    def post(self):
        pass

    def _get_deps_data(self, deps):
        return tuple(map(lambda x: dict(
            id=x.get('id'), name=x.get('name'), avg=self._get_avg(deps.employees)
        ), deps))

    def _get_avg(self, emps):
        return sum(e.salary for e in emps) / len(emps)
