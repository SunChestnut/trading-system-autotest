"""
@Author SunYL
@Time 2023/10/11 17:07
"""

from common.ocr_identify import OcrIdentify
from common.tools import get_img_path


class TestOcrIdentify:

    def test_ocr_identify(self):
        auto_code_01 = get_img_path("code01.png", True, ["authcode"])
        auto_code_02 = get_img_path("code02.png", True, ["authcode"])
        code_01_value = OcrIdentify().identify(auto_code_01)
        code_02_value = OcrIdentify().identify(auto_code_02)
        assert code_01_value == "hb5v"
        assert code_02_value == "captcha"
