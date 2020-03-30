"""Declares schemas for 'employees' route."""


from extensions import MA
from models.employee import Employee


class EmployeeSchema(MA.SQLAlchemyAutoSchema):
    """Schema mapping for 'Employee' model."""

    class Meta:
        model = Employee
        include_fk = True
