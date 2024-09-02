from app import models

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

class Department(SQLAlchemyObjectType):
    class Meta:
        model = models.Department
        interfaces = (relay.Node, )




class Query(graphene.ObjectType):
    node = relay.Node.Field()

    all_departments = SQLAlchemyConnectionField(Department.connection, sort=None)


schema = graphene.Schema(query=Query)
