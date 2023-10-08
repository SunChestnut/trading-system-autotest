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


def sep(path: list[str], add_sep_before: bool = False, add_sep_after: bool = False) -> str:
    """
    使用分隔符拼接任意数量的字符
    :param path:    路径列表，类型为列表
    :param add_sep_before:  是否需要在拼接的路径前加一个分隔符
    :param add_sep_after:   是否需要在拼接的路径后加一个分隔符t
    :return:    完整路径
    """
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path += os.sep
    return all_path


def get_img_path(img_name, contain_subdirectory=False, subdirectory: list[str] = None):
    """
    获取本地目录下存放的商品图片的路径
    :param img_name: 图片名称
    :param contain_subdirectory: 是否包含子目录
    :param subdirectory: 子目录名称
    :return:
    """
    project_path = get_project_path()
    img_dir = sep([project_path, "img"])
    if contain_subdirectory:
        for dir_name in subdirectory:
            img_dir = sep([img_dir, dir_name])
        return sep([img_dir, img_name])

    return sep([project_path, "img", img_name])
