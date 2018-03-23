
import graphene
import json
from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
from . import models

class MessageType(DjangoObjectType):
    class Meta:
        model = models.Message
        filter_fields = {'message': ['icontains']}
        interfaces = (graphene.Node, )

class CreateMessage(graphene.Mutation):
    class Input:
        message = graphene.String()

    form_errors = graphene.String()
    message = graphene.Field(lambda: MessageType)

    @staticmethod
    def mutate(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            return CreateMessage(form_errors=json.dumps('Inicie Sesión por favor!'))
        message = models.Message.objects.create(
            user = info.context.user, message=kwargs.get('message'))
        return CreateMessage(message=message, form_errors=None)


class Mutation(object):
    create_message = CreateMessage.Field()


class Query(object):
    all_messages = graphene.List(MessageType)

    all_messages_filtered = DjangoFilterConnectionField(MessageType)

    def resolve_all_messages(self, info, **kwargs):
        return models.Message.objects.all()

    def resolve_all_messages_filtered(self, info, **kwargs):
        return models.Message.objects.all()