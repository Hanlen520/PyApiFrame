# FileName : login_v1_test.py
# Author   : Adil
# DateTime : 2017/12/10 13:26
# SoftWare : PyCharm

# 从excel读取数据

import unittest,requests

from  Wm_Api.common import Excel
import json

Ex = Excel.Excel()

class LoginTest(unittest.TestCase):
    '''定义登录类'''

    def setUp(self):
        self.base_url = 'https://www.yiyao.cc'
        self.com_url = 'http://bijia.yiyao.cc'

    def tearDown(self):
        pass

    def testComPrice(self):
        '''比价神器'''
        try:
            caseList = Ex.readExcel('ApiInfo.xlsx','ComPrice')

            for caseDict in caseList:
                url = self.com_url + caseDict['ApiLoad']
                method = caseDict['Method']
                caseData = caseDict['CaseData']
                caseRun = caseDict['CaseRun']
                caseName = caseDict['CaseName']
                expectValue = caseDict['ExpectValue']
                caseData = eval(caseData)
                headers = {'content-type': 'application/json; charset=utf8'}
                if caseRun == 'Y':
                    if method == 'Post':
                        print(caseName)
                        keyValue=['感冒']
                        #keyValue.append(caseData(['keyword']))
                        print(keyValue)
                        expectValue = eval(expectValue)
                        caseData = json.dumps(caseData)
                        response = requests.post(url, caseData,headers=headers)
                        self.result = response.json()
                        self.assertEqual(self.result['code'],expectValue['code'],msg=None)
                        self.assertEqual(self.result['hint'],expectValue['hint'],msg=None)
                        #self.assertIn( ['感冒咳嗽颗粒', '感冒安片'],keyValue,msg=None)
                        #self.assertEqual(self.result['message'],expectValue['message'],msg=None)
                        print(self.result)
        except BaseException as msg:
            self.assertIsNone(msg, msg=None)
            print(msg)


    def testLogin(self):
        '''用户登录'''
        try:
            caseList = Ex.readExcel('ApiInfo.xlsx','Login')

            for caseDict in caseList:
                url = self.base_url + caseDict['ApiLoad']
                method = caseDict['Method']
                caseData = caseDict['CaseData']
                caseRun = caseDict['CaseRun']
                caseName = caseDict['CaseName']
                expectValue = caseDict['ExpectValue']
                caseData = eval(caseData)

                if caseRun == 'Y':
                    if method == 'Post':

                        print(caseName)
                        expectValue = eval(expectValue)
                        response = requests.post(url, caseData)
                        self.result = response.json()
                        self.assertEqual(self.result['success'],expectValue['success'],msg=None)
                        self.assertEqual(self.result['error'],expectValue['error'],msg=None)
                        self.assertEqual(self.result['message'],expectValue['message'],msg=None)
                        print(self.result)

                    if method == 'Get':
                        print(caseName)
                        response = requests.get(url, params=caseData)
                        self.result = response.text
                        # self.assertEqual(self.result['success'], expectValue['success'], msg=None)
                        print(self.result)
                        pass

        except BaseException as msg:
            self.assertIsNone(msg, msg=None)
            print(msg)


if __name__ == '__main__':

    unittest.main()