# -*- coding: utf-8 -*-
class User:

    def __init__(self, name=None, login=None, web_password=None, rep_web_password=None, phone=None,
                 sms_password=None, rep_sms_password=None, userAdminAccess=None, egida3Mode=None,
                 TakeOn=None, TakeOff=None, operatorMessRedirect=None):
        self.name = name
        self.login = login
        self.web_password = web_password
        self.rep_web_password = rep_web_password
        self.phone = phone
        self.sms_password = sms_password
        self.rep_sms_password = rep_sms_password
        self.userAdminAccess = userAdminAccess
        self.egida3Mode = egida3Mode
        self.TakeOn = TakeOn
        self.TakeOff = TakeOff
        self.operatorMessRedirect = operatorMessRedirect

    def __repr__(self):
        return "%s" % (self.name)

    def __eq__(self, other):
        return self.name == other.name
