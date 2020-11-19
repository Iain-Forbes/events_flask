from app.models.event import *


event1 = Event("T in the Park", "34/9/23", 1500, "The Park", "Musical Fun Time, in the park")
event2 = Event("Bouncy Castle", "29/9/21", 15, "The Park", "Bouncy Bouncy Castle Time: Come bounce on my castle!")

events = [event1, event2]


def add_new_event(event):
    events.append(event)



