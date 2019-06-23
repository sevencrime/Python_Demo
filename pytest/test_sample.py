import unittest



class BaseTestCase(unittest.TestCase):

	globals()["status"] = "aaaa"


class TestCase1(BaseTestCase):

	def test1_my_dict_key(self):
		print("ddd", globals()["status"])
		globals()["status"] = "bbbb"

	def test2_kkk(self):
		print("kkk", globals()["status"])

class TestCase2(BaseTestCase):

	def test_my_dict_value(self):

		print("uuu", globals()["status"])


if __name__ == "__main__":
	unittest.main()