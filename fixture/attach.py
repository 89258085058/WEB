from dataclasses import dataclass

import allure
from allure_commons.types import AttachmentType


@dataclass
class Attachments:
    app: any

    def add_screenshot(self):
        wd = self.app.wd
        allure.attach(wd.get_screenshot_as_png(), name="↓ СКРИНШОТ ↓", attachment_type=AttachmentType.PNG)

    def add_logs(self):
        wd = self.app.wd
        log = "".join(f'{text}\n' for text in wd.get_log(log_type='browser'))
        allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

    def add_html(self):
        wd = self.app.wd
        html = wd.page_source
        allure.attach(html, 'page_source', AttachmentType.HTML, '.html')

    def add_video(self):
        wd = self.app.wd
        video_url = "https://selenoid.autotests.cloud/video/" + wd.session_id + ".mp4"
        html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
               + video_url \
               + "' type='video/mp4'></video></body></html>"
        allure.attach(html, 'video_' + wd.session_id, AttachmentType.HTML, '.html')
