# -*- coding: utf-8 -*-
import requests
from dataclasses import dataclass

base_url = "http://192.168.22.169/signal/journal/80340089"


@dataclass
class EndpointHelper:
    app: any

    # EvtFromSensors, EvtFromKeyChain
    def generate_json(self, p_event, z_event, event_type):
        data = {
            "journal": {
                           "Event": {
                               "P_Event": p_event,
                               "PartitionsMask": 2,
                               "SourceID": 1,
                               "UserID": 0,
                               "Z_Event": z_event,
                               "NotTakenSensors": [4],
                               "NotTakeFireFlag": 1,
                               "TemporaryDisabledSensors": [4]
                           },
                           "EventType": event_type,
                       } | self.common_json
        }
        return data

    def generate_json_climate(self, p_event, z_event, event_type, value_type_evt):
        data = {
            "journal": {
                           "Event": {
                               "P_Event": p_event,
                               "PartitionsMask": 2,
                               "SourceID": 1,
                               "UserID": 0,
                               "Z_Event": z_event,
                               "temperature": 30,
                               "humidity": 55,
                               "CO": 700,
                               "evtType": value_type_evt
                           },
                           "EventType": event_type,
                       } | self.common_json
        }
        return data

    def create_event(self, data):
        wd = self.app.wd
        requests.post(f'{base_url}/generate/', json=data)
        wd.refresh()

    def delete_all_events(self):
        wd = self.app.wd
        requests.delete(f'{base_url}/delete/')
        wd.refresh()

    def generate_json_for_evt_from_key(self, p_event):
        data = {
            "journal": {
                           "Event": {
                               "P_Event": p_event,
                               "PartitionsMask": 2,
                               "SourceID": 1,
                               "UserID": 0,
                               "KeyID": 1,
                               "NotTakenSensors": [4],
                               "NotTakeFireFlag": 1,
                               "TemporaryDisabledSensors": [4]
                           },
                           "EventType": 3,
                       } | self.common_json
        }
        return data

    '''Json для приборов'''

    common_json = {
        "EventID": 0,
        "timeZone15Min": 12,
        "datetime": 1641038690,
        "UserName": "Test"
    }

    def generate_json_for_bl(self, value):
        data = {
            "journal": {
                           "Event": {
                               "PreviousSwVer": 256,
                               "NewSwVer": 284,
                               "BlEvent": value,
                               "UserID": 0
                           },
                           "EventType": 9,
                       } | self.common_json
        }
        return data

    def generate_json_for_fw(self, value):
        data = {
            "journal": {
                           "Event": {
                               "PreviousSwVer": 256,
                               "NewSwVer": 284,
                               "event": value,
                               "UserID": 0
                           },
                           "EventType": 11,
                       } | self.common_json
        }
        return data

    def generate_json_for_time_sync(self, value):
        data = {
            "journal": {
                           "Event": {
                               "event": value,
                               "UserID": 0
                           },
                           "EventType": 15
                       } | self.common_json
        }
        return data

    def generate_json_for_ps(self, value):
        data = {
            "journal": {
                           "Event": {
                               "PowerStatus": value,
                           },
                           "EventType": 6,
                       } | self.common_json
        }
        return data

    def generate_json_for_login(self, value_login_status, value_type_auth):
        data = {
            "journal": {
                           "Event": {
                               "LogInStatus": value_login_status,
                               "AuthorizationType": value_type_auth,
                               "UserID": 0
                           },
                           "EventType": 10,
                       } | self.common_json
        }
        return data

    def generate_json_for_gsm_module(self, value_event):
        data = {
            "journal": {
                           "Event": {
                               "GsmStatusEvent": value_event,
                               "simNumber": 1,
                               "OperatorName": "Megafon",
                               "numberAttempts": 2
                           },
                           "EventType": 8,
                       } | self.common_json
        }
        return data

    def generate_json_for_channel(self, value_status):
        data = {
            "journal": {
                           "Event": {
                               "eventId": 1,
                               "eventIndex": 1,
                               "attemptCount": 1,
                               "channelIndex": 1,
                               "directionIndex": 1,
                               "currentStatus": value_status
                           },
                           "EventType": 12,
                       } | self.common_json
        }
        return data

    def generate_json_for_text_string(self, value_source):
        data = {
            "journal": {
                           "Event": {
                               "text": "Text SMS - Hello world",
                               "source": value_source,
                               "user": 0
                           },
                           "EventType": 19,
                       } | self.common_json
        }
        return data

    def generate_json_for_output(self, value_out_event_type, value):
        data = {
            "journal": {
                           "Event": {
                               "OutEventType": value_out_event_type,
                               "SourceID": 1,
                               "OutNum": 100,
                               "FaultState": value,
                               "OutState": value,
                               "MaskEvent": value
                           },
                           "EventType": 5,
                       } | self.common_json
        }
        return data

    def generate_json_for_system(self, value_sys_evt_type, value=0):
        data = {
            "journal": {
                           "Event": {
                               "SysEvtType": value_sys_evt_type,
                               "SysObjectID": 5,
                               "SysEventUserID": 0,
                               "SensorType": value,
                               "KeyID_HEX": 12345672,
                               "control_p_mask": 555552,
                               "AccessLaw": value,
                               "Balance": "123",
                               "phoneNumber": 89167115944
                           },
                           "EventType": 7,
                       } | self.common_json
        }
        return data

    def generate_json_for_system_standard(self, value_sys_evt_type):
        data = {
            "journal": {
                           "Event": {
                               "SysEvtType": value_sys_evt_type,
                               "SysObjectID": 5,
                               "SysEventUserID": 0,
                               "channel0Type": 0,
                               "channel1Type": 2,
                               "channel2Type": 1,
                               "Balance": 100,
                               "phoneNumber": 89167115555
                           },
                           "EventType": 7,
                       } | self.common_json
        }
        return data

    def generate_json_for_system_add_delete_user(self, value_sys_evt_type, value_settings_changes):
        data = {
            "journal": {
                           "Event": {
                               "SysEvtType": value_sys_evt_type,
                               "SysObjectID": 5,
                               "SysEventUserID": 0,
                               "settingsChanges": value_settings_changes
                           },
                           "EventType": 7,
                       } | self.common_json
        }
        return data

    def generate_json_for_system_case_state(self, value_sys_evt_type, value_case_state, value_p_event):
        data = {
            "journal": {
                           "Event": {
                               "SysEvtType": value_sys_evt_type,
                               "SysObjectID": 5,
                               "SysEventUserID": 0,
                               "CaseOpenState": value_case_state,
                               "P_Event": value_p_event
                           },
                           "EventType": 7,
                       } | self.common_json
        }
        return data

    def generate_json_for_assert_filters(self, p_event, z_event, event_type, time, name):
        data = {
            "journal": {
                "Event": {
                    "P_Event": p_event,
                    "PartitionsMask": 2,
                    "SourceID": 1,
                    "UserID": 0,
                    "Z_Event": z_event
                },
                "EventType": event_type,
                "EventID": 0,
                "timeZone15Min": 12,
                "datetime": time,
                "UserName": name
            }
        }
        return data

    def create_event_for_filters(self, p_event, z_event, event_type, time, name):
        data = self.generate_json_for_assert_filters(p_event, z_event, event_type, time, name)
        requests.post(f'{base_url}/generate/', json=data)

    def generate_json_for_test(self, value_test_type, value_state, value_channel):
        data = {
            "journal": {
                           "Event": {
                               "datetime": 1661221727,
                               "direction": 1,
                               "channel": value_channel,
                               "state": value_state,
                               "testType": value_test_type
                           },
                           "EventType": 16,
                       } | self.common_json
        }
        return data
