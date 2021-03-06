from views.base import Base


class Departments(Base):
    def __init__(self, templates, api_url):
        super().__init__(templates, api_url)

    def _transform_many(self, entities):
        return tuple(map(lambda x: dict(
            id=x.get('id'),
            name=x.get('name'),
            emps_num=len(x.get('employees')),
            avg=self._get_avg(x.get('employees'))
        ), entities))

    def _transform_one(self, entity):
        return entity

    def _get_avg(self, emps):
        return sum(e.get('salary') for e in emps) / len(emps)
