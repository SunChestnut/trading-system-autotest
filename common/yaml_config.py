"""
@Author SunYL
@Time 2023/9/12 16:13
"""

import yaml

from common.tools import get_project_path, sep


class GetConf:

    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_username_password(self, user_info):
        return self.env["users"][user_info]["username"], self.env["users"][user_info]["password"]

    def get_mysql(self):
        return self.env["mysql"]

    def get_url(self):
        return self.env["url"]

    def get_mysql_config(self):
        return self.env["mysql"]
