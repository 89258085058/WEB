# -*- coding: utf-8 -*-
import json
import os


class DataHelper:

    def __init__(self, app):
        self.app = app

    def data_all(self):
        f = "data/db_data.json"
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False)

    def data_object(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["object"]

    def data_radio(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["Radio"]

    def data_ethernet(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["Ethernet"]

    def data_volum_indication(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["VolumIndication"]

    def data_date_time(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["DateTime"]

    def data_gsm(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["GSM"]

    def data_out(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["Out"]

    def data_path(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["Path"]

    def data_directions(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["Directions"]

    def data_user(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["User"]

    def data_key(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["Key"]

    def data_brelok(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["Brelok"]

    def data_c_2000p_ik(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["C_2000P_IK"]

    def data_c_2000p_smk(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["C_2000P_SMK"]

    def data_sensor_kc(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["SENSOR_KC"]

    def data_sensor_sdvig(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["C_2000P_SDVIG"]

    def data_sensor_c_2000p_ip(self):
        data = self.data_all()
        json_data = json.loads(data)
        return json_data["C_2000P_IP"]
