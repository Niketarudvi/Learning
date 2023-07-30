from selenium import webdriver
import pytest
import allure
# class Test_Credence_001:
#
#     def test_sum_001(self):
#         a = 3
#         b = 7
#         sum = a + b
#         print("Sum of a and b is :" + str(sum))
#         if sum == 10:
#             assert True
#         else:
#             assert False
#
#     def test_CredenceUrl_002(self):
#         driver = webdriver.Chrome()
#         driver.get("https://credence.in/")
#         if driver.title == "Credence":
#             print("You are at credence.in")
#             assert True
#             driver.close()
#         else:
#             print("You are at Wrong url")
#             driver.close()
#             assert False
#
#
#     def test_sub_003(self):
#         a = 8
#         b = 7
#         sub = a - b
#         print("Subtraction of a from b is :" + str(sub))
#         if sub == 1:
#             assert True
#         else:
#             assert False
# from selenium import webdriver


class Test_001:
    def test_Credence_001(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            driver.save_screenshot("D:\\Python\\Pytest_July0\\Screenshot\\Credence.PNG")
            driver.close()
            assert True
        else:
            print("You are at wrong place")
            driver.close()
            assert False


    # def test_sum_002(self):
    #     a = 2
    #     b = 5
    #     sum = a+b
    #     print("This is sum of a&b: " + str(sum))
    #     if sum == 7:
    #         assert True
    #     else:
    #         assert False
    #

# pytest -v --html=Reports/myreport.html -n=2 --alluredir="D:\Credence Class Notes\CredenceBatches\CredenceBatch#14 & 15\Pytest_Demo\AllureReports"



