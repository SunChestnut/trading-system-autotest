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
            # print(type(self.env))  # output: <class 'dict'>
            # print(type(self.env["mysql"]), self.env["mysql"])
            # print(self.env["mysql"]["db"])

    def get_username_password(self, user_info):
        return self.env["users"][user_info]["username"], self.env["users"][user_info]["password"]

    def get_mysql(self):
        return self.env["mysql"]

    def get_url(self):
        return self.env["url"]


if __name__ == '__main__':
    print("username & password:", GetConf().get_username_password("zjl"))  # zjl,周杰伦
    print(GetConf().get_mysql())
    print(GetConf().get_url())
