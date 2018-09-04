"""
slackに関するモジュール
"""

import requests


class Slack(object):
    """
    Slack関連クラス
    """

    def __init__(self, logger, token, channel):
        # type: (logger, str, str) -> None
        """
        slack設定のコンストラクタ
        :param logger: logger
        :param token: slackのtoken
        :param channel: 投稿先チャンネル名
        """
        self.logger = logger
        self.token = token
        self.channel = channel

    def notify_with_figure(self, massage, abs_figure_path):
        # type: (str, str) -> None
        """
        slackにメッセージと画像を投稿する
        :param massage: 投稿内容
        :param abs_figure_path: 保存した画像の絶対パス
        """
        self.logger.info('notify_with_figure')

        files = {'file': open(abs_figure_path, 'rb')}

        param = {
            'token': self.token,
            'channels': self.channel,
            'filename': "filename",
            'initial_comment': massage,
            'title': "todays btc MACD"
        }

        requests.post(url="https://slack.com/api/files.upload", params=param, files=files)
