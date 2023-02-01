import telebot
from telebot import apihelper
from telebot.types import InputMediaPhoto
from matplotlib import pyplot as plt
import json
import os


class CreateAllure:

    def data_alure_report_artifacts(self):
        f = "allure-report/widgets/summary.json"
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False)

    def data_statistic(self):
        data = self.data_alure_report_artifacts()
        json_data = json.loads(data)
        return json_data["statistic"]

    def config_file(self):
        f = "notifications/config.json"
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False)

    def data_config(self):
        data = self.config_file()
        json_data = json.loads(data)
        return json_data["base"]

    def create_data(self):
        self.failed = self.data_statistic()['failed']
        self.broken = self.data_statistic()['broken']
        self.passed = self.data_statistic()['passed']
        self.skipped = self.data_statistic()['skipped']
        self.total = self.data_statistic()['total']
        self.name = self.data_config()['project']
        self.proxy = self.data_config()['proxy']
        self.token = self.data_config()['token']
        self.chat = self.data_config()['chat']
        self.reportLink = self.data_config()['reportLink']
        labels = ['Прошедшие', 'Упавшие', 'Ошибки', 'Пропущеные']
        values = [self.passed, self.failed, self.broken, self.skipped]
        colors = ['green', 'red', 'yellow', 'grey']
        explode = [0.2, 0, 0, 0]
        plt.title(f'{self.name}')
        plt.pie(values, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%1.1f%%', startangle=180)
        plt.axis('equal')
        return plt.savefig('allure_bot/allure.png')

    def send_messege(self):
        try:
            self.create_data()
            bot = telebot.TeleBot(f'{self.token}')
            bot.send_media_group(f'{self.chat}', [InputMediaPhoto(open('allure_bot/allure.png', 'rb'),
                                                                  caption=f'Рабочее окружение: Удаленный интерфейс ПО SignalGSM'
                                                                          f'\n'
                                                                          f'\nВсего тестов: {self.total}'
                                                                          f'\nУспешных тестов: {self.passed}'
                                                                          f'\nУпавших тестов: {self.failed}'
                                                                          f'\nНеисправных тестов: {self.broken}'
                                                                          f'\nПропущенных тестов: {self.skipped}'
                                                                          f'\nОтчет: {self.reportLink}')])
        except:
            self.create_data()
            apihelper.proxy = {'https': f'{self.proxy}'}
            bot = telebot.TeleBot(f'{self.token}')
            bot.send_media_group(f'{self.chat}', [InputMediaPhoto(open('allure_bot/allure.png', 'rb'),
                                                                  caption=f'Рабочее окружение: Удаленный интерфейс ПО SignalGSM'
                                                                          f'\n'
                                                                          f'\nВсего тестов: {self.total}'
                                                                          f'\nУспешных тестов: {self.passed}'
                                                                          f'\nУпавших тестов: {self.failed}'
                                                                          f'\nНеисправных тестов: {self.broken}'
                                                                          f'\nПропущенных тестов: {self.skipped}'
                                                                          f'\nОтчет: http://194.67.118.210:8080/job/Signal_ui/allure/#behaviors')])


messege = CreateAllure()
messege.send_messege()
