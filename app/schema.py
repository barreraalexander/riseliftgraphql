import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import db_session, Department as DepartmentModel, Employee as EmployeeModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class DepartmentGQL(graphene.ObjectType):
    name = graphene.String()
    id = graphene.Int()

class CreateDepartment(graphene.Mutation):
    class Arguments:
        name = graphene.String()


    Output = DepartmentGQL


    def mutate(root, info, name):

        department_dict = {
            "name" : name
        }

        new_department = DepartmentModel(**department_dict)

        db_session.add(new_department)
        db_session.commit()
        db_session.refresh(new_department)
        db_session.close()
        
        return new_department




class MyMutations(graphene.ObjectType):
    create_department = CreateDepartment.Field()

class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )

    # class Arguments:
    #     name = graphene.String()


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_employees = SQLAlchemyConnectionField(Employee.connection)
    # Disable sorting over this field
    all_departments = SQLAlchemyConnectionField(Department.connection, sort=None)



schema = graphene.Schema(query=Query, mutation=MyMutations)