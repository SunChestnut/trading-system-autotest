"""
@Author SunYL
@Time 2023/9/12 16:13
"""
import os.path


def get_project_path() -> str:
    """
    获取项目的绝对路径
    :return:
    """
    project_name = "trading-system-autotest"
    # 获取当前模块的绝对路径
    file_path = os.path.dirname(__file__)
    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path: list[str], add_sep_before=False, add_sep_after=False) -> str:
    """
    使用分隔符拼接任意数量的字符
    :param path:    路径列表，类型为列表
    :param add_sep_before:  是否需要在拼接的路径前加一个分隔符
    :param add_sep_after:   是否需要在拼接的路径后加一个分隔符
    :return:    完整路径
    """
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path += os.sep
    return all_path


def get_img_path(img_name):
    """
    获取本地目录下存放的商品图片的路径
    :param img_name: 图片名称
    :return:
    """
    project_path = get_project_path()
    return sep([project_path, "img", img_name], False, False)


if __name__ == '__main__':
    # print(get_project_path())
    # print(sep(["config", "environment.yaml"], True, True))
    print(get_img_path("img-01.jpg"))
