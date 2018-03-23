import graphene
import message.schema
import wrapApi.schema

class Mutation(message.schema.Mutation, graphene.ObjectType):
    pass


class Query(message.schema.Query, wrapApi.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)