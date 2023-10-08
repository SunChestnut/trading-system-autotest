"""
@Author SunYL
@Time 2023/9/26 17:56
"""
import aircv


class FindImage:

    def read_image(self, image_path):
        """
        读取图片
        :param image_path: 图片路径
        :return:
        """
        return aircv.imread(image_path)

    def get_confidence(self, source_path, search_path):
        """
        通过「模板匹配」的方式查找图片
        :param source_path: 原图路径
        :param search_path: 需要查找的图片的路径
        :return:
        """
        image_src = self.read_image(source_path)
        image_dest = self.read_image(search_path)
        result = aircv.find_template(image_src, image_dest)
        print("search image: ", result)
        return result["confidence"]

    def get_pic_with_sift(self, source_path, search_path):
        """
        通过「特征匹配」的方式查找图片。SIFT, Scale Invariant Feature Transform,尺度不变特征转换
        :param source_path:
        :param search_path:
        :return:
        """
        image_src = aircv.imread(source_path)
        image_dest = aircv.imread(search_path)
        result = aircv.find_sift(image_src, image_dest)
        print("search image: ", result)
