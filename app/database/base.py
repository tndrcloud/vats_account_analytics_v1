# Import all the models, so that Base has them before being
# imported by Alembic

from app.database.base_class import Base 
from app.models.models import Role
from app.models.models import User  
from app.models.models import Data
