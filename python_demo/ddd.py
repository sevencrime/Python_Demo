#! /usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import ast
import time
import json
from bson.objectid import ObjectId
import datetime


def to_json(data):
    return json.dumps(data, sort_keys=True, indent=4, separators=(', ', ': '), cls=JSONEncoder)

class JSONEncoder(json.JSONEncoder):
    """处理ObjectId & datetime类型无法转为json"""
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime.datetime):
            return datetime.datetime.strftime(o, '%Y-%m-%d %H:%M:%S')

        return json.JSONEncoder.default(self, o)


data = {'_id': ObjectId('5e5db5767cba990010f010f1'), 'currentStep': '/account-opening-status', 'customerSource': 'H5', 'area': 'CHN', 'country': 'CHN', 'totalAnnualCustomerRevenueHKSource': [], 'customerNetAssetValueHKSource': [], 'sourceOfWealth': ['savings', 'selfOperated', 'investment'], 'purposeOfInvestment': ['speculation', 'hedging', 'asset'], 'accountType': ['securitiesCash', 'futuresMargin'], 'isBondFuturesClientsConnected': 'N', 'liveChecked': True, 'caApplyErr': ['getPdfInfoForSign:-24:证书遗失补办失败:2020-3-3 9:46:32'], 'auditStatus': 'passed', 'submitCount': 1, 'rejectedReason': [], 'phone': '15033332222', 'referralCode': '', 'learnHowCode': 'EDAA', 'referrerUrl': 'https://eddid-ali-idp-uat.ntdev.be:8443/session/end?id_token_hint=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJwSEdUcXlqa1d1Y3pGenVEU0p0OFJnSjBuZW0yMmhVVWtJQlFIVFA3VjAifQ.eyJzdWIiOiJkMzJiZmE1YS1lOTFkLTRmZWQtYmYxNi02MGM5MTRlNWYyNzEiLCJ1cGRhdGVkX2F0IjoiMjAyMC0wMi0yNVQwNzoxMDo1OC42NDdaIiwiZW1haWwiOiIxMzQ4MDk5NDM4N0B0b2JlbGVhZC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGhvbmVfbnVtYmVyIjoiODYxMzQ4MDk5NDM4NyIsInBob25lX251bWJlcl92ZXJpZmllZCI6dHJ1ZSwicm9sZXMiOltdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiIxMzQ4MDk5NDM4NyIsImN1c3RvbSI6eyJkZXZpY2VfaWQiOiIiLCJzeW5jRmxhZyI6Miwic3luY1RpbWUiOjE1ODI2MTQ2NTkwNzIsInN5bmNTdWNjZXNzVGltZSI6MTU4MjYxNDY1OTg1N30sIm5vbmNlIjoiOWQwNWNlMjhmZDkyNDcyYTkyNTFmN2ZiNTIyYTBhYmIiLCJzaWQiOiI3YTQ3MzYyNS1iMTgyLTRmYjUtYmMzZS00Yzc2M2JlMmU1NjYiLCJhdF9oYXNoIjoiLUw3Q3lJWTJCLTVZZTlqZVlsbi1ZZyIsInNfaGFzaCI6Il9FRVFWWnFsOWcyMkFMcnRLdWxWMkEiLCJhdWQiOiJhb3MtaDUiLCJleHAiOjE1ODI2NjA1NjQsImlhdCI6MTU4MjYxNzM2NCwiaXNzIjoiaHR0cHM6Ly9lZGRpZC1hbGktaWRwLXVhdC5udGRldi5iZTo4NDQzIn0.gpLiOSj8fKQbe66i7YjQPx816SsPIA_RYba7RVsqmPEWZCZaacWZtNinIDhntGfMu_OV7Irs6P-BVIOWib3EZcdWq_VzKQJvwWdUPrkxaIZCQI4MiVnnXut6ONm0Y7_J4V8hX1QAaQkcj33pT5sQr4pSOJgn361uh-mSPPkI_wGbIAp3h-PGSwFG3bnyECR8iDx91VQ70eMsxphPokCIKkeJ5SvN8vseNHvBAi1nZ-Nu6gFWdlgO9cC4Ps8zhtpN23JS5i2URql3Za2LlMWr9Vz2mavzJ6Bs7uxWHfEq0CTXnFmOnI8AyIBKC_7O-3JXJ257w34W2hZ-rf9RQVCvoA&post_logout_redirect_uri=https%3A%2F%2Faos-h5-uat.ntdev.be%3A8443&sign_up_uri=https%3A%2F%2Faos-h5-uat.ntdev.be%3A8443&sign_in_default_phone=', 'locationUrl': 'https://aos-h5-uat.ntdev.be:8443/', 'phoneAreaCode': '+86', 'idpId': '8741041b-53a8-4bf5-967d-808988f163b6', 'idpEmail': '13480994387@tobelead.com', 'applyCode': 'h58259', 'latestPlatform': 'H5', 'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A346 Safari/602.1', 'bankAccount': [], 'createdAt': datetime.datetime(2020, 3, 3, 1, 40, 6, 804000), 'updatedAt': datetime.datetime(2020, 3, 3, 1, 50, 18, 109000), '__v': 1, 'birthday': 536212800000.0, 'chineseName': '鄂孔杰', 'email': '15033332222@123.com', 'gender': 0, 'idCardAddress': '重庆市万州区宁波路201号1幢7-4', 'idCardExpireAt': '2036.06.21', 'idCardFrontImg': 'sync/aos/d934a704-1843-4785-8d88-69d98ed8d1ca.JPG', 'idCardIssuedBy': '重庆市公安局万州分局', 'idCardReverseImg': 'sync/aos/5d901de3-9c64-446f-a695-17c488062ce3.JPG', 'idCardValidateAt': '2016.06.21', 'idNumber': '441502199502122334', 'pinyinFirstName': 'Kongjie', 'pinyinLastName': 'E', 'authBankAccount': {'_id': ObjectId('5e5db6817cba990010f010f2'), 'name': '农业', 'number': '6228480478396439679', 'phone': '15823114387'}, 'businessAddress': '测试', 'businessTypeOpt': '文化 、体育或娱乐', 'businessTypeOther': '', 'employer': '测试', 'employment': 'self', 'isRegisteredCompany': 'Y', 'occupation': '测试', 'CBBC': 'lt1Year', 'customerNetAssetValueHK': 'lt1000000', 'customerNetAssetValueHKImg': '', 'customerNetAssetValueHKOther': '', 'futures': '1To5Years', 'options': 'lt1Year', 'otherInvestment': '', 'otherInvestmentText': '', 'riskTolerance': 'high', 'securities': '1To5Years', 'sourceOfWealthOther': '', 'totalAnnualCustomerRevenueHK': 'lt200000', 'totalAnnualCustomerRevenueHKImg': '', 'totalAnnualCustomerRevenueHKOther': '', 'warrants': 'lt1Year', 'isApplyToOpenTradingStructure': 'Y', 'isIndustryExperience': 'N', 'isLearnAboutProducts': 'Y', 'isStocks': 'Y', 'tradingStructureRiskChecked': 'Y', 'isAcquaintHighLevel': 'N', 'isAmericanResidents': 'N', 'isAmericanResidentsb': 'N', 'isBankruptcy': 'N', 'isBeneficiary': 'Y', 'isInAgtJobs': 'N', 'isOrders': 'Y', 'isPoliticalFigure': 'N', 'salesAgreed': 'Y', 'riskDisclosureChecked': 'Y', 'signatureChecked': 'Y', 'liveImageOssName': 'aos/livings/2020.3/鄂孔杰.500101198612296436.faceid15831999007045444.jpg', 'signatureImg': 'sync/aos/ebddb1ed-a629-4dd1-91b8-776bc0c095ef.png', 'submitTime': datetime.datetime(2020, 3, 3, 1, 46, 32, 995000), 'rejectedRemark': ''}
data1 = [{'_id': ObjectId('5e5db575f352d600103c7cb6'), 'email_verified': True, 'phone_number_verified': True, 'roles': [], 'enabled': True, 'preferred_username': '15033332222', 'email': '15033332222@123.com', 'phone_number': '8615033332222', 'custom': {'device_id': '', 'syncFlag': 2, 'syncTime': 1583199605806.0, 'syncSuccessTime': 1583199607177.0, 'accountNumber': '10216', 'accountId': '5e5db7d80f87786fb77595de'}, 'subject': '8741041b-53a8-4bf5-967d-808988f163b6', 'created_at': datetime.datetime(2020, 3, 3, 1, 40, 5, 701000), 'updated_at': datetime.datetime(2020, 3, 3, 1, 50, 17, 720000), 'secret': '$2a$08$.krA3sL3Zil3njm.u6V/4uijIcaP9by.Nsfh/MFRv.W6WjLw6o0ma', '__v': 0, 'address': '重庆市万州区宁波路201号1幢7-4', 'birthdate': '1986-12-29T04:00:00.000Z', 'family_name': 'E', 'gender': 'm', 'given_name': 'Kongjie', 'locale': 'zh-hans', 'name': 'Kongjie E', 'zoneinfo': 'CHN'}, {'_id': ObjectId('5e5db575f352d600103c7cb6'), 'email_verified': True, 'phone_number_verified': True, 'roles': [], 'enabled': True, 'preferred_username': '15033332222', 'email': '15033332222@123.com', 'phone_number': '8615033332222', 'custom': {'device_id': '', 'syncFlag': 2, 'syncTime': 1583199605806.0, 'syncSuccessTime': 1583199607177.0, 'accountNumber': '10216', 'accountId': '5e5db7d80f87786fb77595de'}, 'subject': '8741041b-53a8-4bf5-967d-808988f163b6', 'created_at': datetime.datetime(2020, 3, 3, 1, 40, 5, 701000), 'updated_at': datetime.datetime(2020, 3, 3, 1, 50, 17, 720000), 'secret': '$2a$08$.krA3sL3Zil3njm.u6V/4uijIcaP9by.Nsfh/MFRv.W6WjLw6o0ma', '__v': 0, 'address': '重庆市万州区宁波路201号1幢7-4', 'birthdate': '1986-12-29T04:00:00.000Z', 'family_name': 'E', 'gender': 'm', 'given_name': 'Kongjie', 'locale': 'zh-hans', 'name': 'Kongjie E', 'zoneinfo': 'CHN'}, {'_id': ObjectId('5e5db575f352d600103c7cb6'), 'email_verified': True, 'phone_number_verified': True, 'roles': [], 'enabled': True, 'preferred_username': '15033332222', 'email': '15033332222@123.com', 'phone_number': '8615033332222', 'custom': {'device_id': '', 'syncFlag': 2, 'syncTime': 1583199605806.0, 'syncSuccessTime': 1583199607177.0, 'accountNumber': '10216', 'accountId': '5e5db7d80f87786fb77595de'}, 'subject': '8741041b-53a8-4bf5-967d-808988f163b6', 'created_at': datetime.datetime(2020, 3, 3, 1, 40, 5, 701000), 'updated_at': datetime.datetime(2020, 3, 3, 1, 50, 17, 720000), 'secret': '$2a$08$.krA3sL3Zil3njm.u6V/4uijIcaP9by.Nsfh/MFRv.W6WjLw6o0ma', '__v': 0, 'address': '重庆市万州区宁波路201号1幢7-4', 'birthdate': '1986-12-29T04:00:00.000Z', 'family_name': 'E', 'gender': 'm', 'given_name': 'Kongjie', 'locale': 'zh-hans', 'name': 'Kongjie E', 'zoneinfo': 'CHN'}]
# data = JSONEncoder().encode(data)

# print(to_json(json.loads(JSONEncoder().encode(data))))
# print(to_json(data))

# json.loads(JSONEncoder().encode(_d))

# print(to_json(data1))
print(type(data1))



