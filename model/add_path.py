# -*- coding: utf-8 -*-
class Path:

    def __init__(self, number=None, name=None, auto_take_from_no_take=None, auto_take_from_alarm=None, delayed_take=None):
        self.name = name
        self.number = number
        self.auto_take_from_no_take = auto_take_from_no_take
        self.auto_take_from_alarm = auto_take_from_alarm
        self.delayed_take = delayed_take

    def __repr__(self):
        return "%s" % (self.number)

    def __eq__(self, other):
        return self.number == other.number
