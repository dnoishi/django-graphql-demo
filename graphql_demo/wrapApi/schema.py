import requests 
import json
import os
import graphene
from collections import namedtuple
from graphene import ObjectType, String, Boolean, ID, Field, Int, List
from graphene.types.datetime import Date, DateTime

def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

class User(ObjectType):
    login = String()
    id = Int()
    avatar_url = String()
    gravatar_id = String()
    url = String()
    html_url = String()
    followers_url = String()
    following_url = String()
    gists_url = String()
    starred_url = String()
    subscriptions_url = String()
    organizations_url = String()
    repos_url = String()
    events_url = String()
    received_events_url = String()
    type = String()
    site_admin = Boolean()
    name = String()
    company = String()
    blog = String()
    location = String()
    email = String() 
    hireable = Boolean()
    bio = String() 
    repos = Int()
    gists = Int()
    followers = Int()
    following = Int()
    created_at = DateTime()
    updated_at = DateTime()

class Query(ObjectType):
    users = List(User)

    def resolve_users(self, info, **kwargs):
        resp = requests.get('https://api.github.com/users', headers={'Accept': 'application/json'})
        return json2obj(json.dumps(resp.json()))