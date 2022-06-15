
import pytest

from utils.encrypt import Encryption


class TestMLKNN:


    @pytest.mark.parametrize(
            "data,enc_data",
            [
                ("hello world", b'gAAAAABimSUCtkhy_H6kWcrZJZJ5AFCZW4x29k1q0Gnjs92jacPPyBwxiTJIzHaAQi3VVEoG7jCeMa2V07VA1JIjrP_ua6GgcQ=='),
            ]
    )
    def test_encryption(self,data,enc_data):
        enc= Encryption('my_password')
        assert enc_data ==enc.encrypt_data(data)