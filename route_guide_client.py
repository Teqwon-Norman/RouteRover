from __future__ import print_function

import logging
import random

import grpc
import route_guide_pb2
import route_guide_pb2_grpc
import route_guide_resources


def make_route_note(message, latitude, longitude):
    return route_guide_pb2.RouteNote(
        message=message,
        location=route_guide_pb2.Point(latitude=latitude, longitude=longitude)
    )

def guide_get_one_feature():
    pass

def guide_get_feature():
    pass

def guide_list_features():
    pass

def generate_route():
    pass

def guide_record_route():
    pass

def generate_messages():
    pass

def guide_route_chat():
    pass

def run():
    pass
