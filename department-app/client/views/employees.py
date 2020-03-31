from views.base import Base


class Employees(Base):
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
        raise NotImplementedError
