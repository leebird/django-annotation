from django.db import models
from .argument_role import ArgumentRole
from .relation import Relation
from .entity import Entity

class EntityAsArgument(models.Model):
    class Meta:
        db_table = 'tm_entity_as_argument'

    # The role that the argument plays in the relation.
    role = models.ForeignKey(ArgumentRole, db_index=True)
    # The relation that the arugment participates.
    relation = models.ForeignKey(Relation, related_name='entity_arguments', db_index=True)
    # The actual entity of the argument.
    argument = models.ForeignKey(Entity, db_index=True)

    def __str__(self):
        return str((self.relation, self.argument, self.role))

    def __repr__(self):
        return self.__str__()
