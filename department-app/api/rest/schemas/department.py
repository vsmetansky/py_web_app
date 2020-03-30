"""Declares schemas for 'departments' route."""

from extensions import MA
from models.department import Department


class DepartmentSchema(MA.SQLAlchemyAutoSchema):
    """Schema mapping for 'Department' model."""
    
    class Meta:
        model = Department
        include_fk = True
