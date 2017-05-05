#!/usr/bin/env python
import unittest
import requests
import json


class DummyTests(unittest.TestCase):
    headers = {}

    #Creating token
    def test_4(self):
        url = "http://138.68.95.151:8080/rest/survey/v1/auth/simple"

        payload = "{\n  \"clientName\": \"string\",\n  \"email\": \"string\",\n  \"facebookId\": \"string\",\n  \"flag\": \"string\",\n  \"googleId\": \"string\",\n  \"id\": 0,\n  \"password\": \"string\",\n  \"token\": \"string\"\n}"
        headers = {
            'content-type': "application/json"
        }
        r = requests.request("POST", url, data=payload, headers=headers)

        self.assertEqual(r.status_code, 200)
        print("[PASSED] Response code 200==200")
        print(r.text)

    #Creating new client - with name and email
    def test_5(self):

        url = "http://138.68.95.151:8080/rest/survey/v1/client/"

        payload = "{\n  \"clientName\": \"ddd\",\n  \"email\": \"ddd@gmail.com\",\n  \"facebookId\": \"string\",\n  \"flag\": \"string\",\n  \"googleId\": \"string\",\n  \"id\": 24078,\n  \"password\": \"string1\",\n  \"token\": \"4efa1956-64c8-46c2-b18b-ffff0e21d6de\"\n}\n\n"
        headers = {
            'content-type': "application/json",
            'accept': "application/json",
            'token': "4efa1956-64c8-46c2-b18b-ffff0e21d6de"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        print(response.text)

    #Change client name
    def test_6(self):
        import requests

        url = "http://138.68.95.151:8080/rest/survey/v1/client/password/24078/"

        payload = "{\n  \"clientName\": \"dpa\"\n}"
        headers = {
            'content-type': "application/json",
            'accept': "application/json",
            'token': "dbe58493-3f03-44d9-abf3-214fc13a5618",
        }

        response = requests.request("PUT", url, data=payload, headers=headers)

        print("[PASSED] Response code 200==200")

        print(response.text)

    #Search client by password
    def test_6(self):

        url = "http://138.68.95.151:8080/rest/survey/v1/client/search/24078/"

        headers = {
            'accept': "application/json",
            'token': "fa3123ae-01d1-41c9-b360-e5f507e6a1bb",
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    #Change client name - and searching by id
    def test_7(self):

        url = "http://138.68.95.151:8080/rest/survey/v1/client/24078/"

        payload = "{\n\t\"clientName\": \"string1\"\n}"
        headers = {
            'accept': "application/json",
            'token': "2922f5ad-527e-4917-8561-a51a3dde58ef",
            'content-type': "application/json"
        }

        response = requests.request("PUT", url, data=payload, headers=headers)
        print("[PASSED] Response code 200==200")
        print(response.text)

    #Deleting user and searching by id
    def test_8(self):

        url = "http://138.68.95.151:8080/rest/survey/v1/client/24078/"

        headers = {
            'accept': "application/json",
            'token': "cb6d2194-0f9f-4823-a59d-3a00cae80fcc"
        }

        response = requests.request("DELETE", url, headers=headers)
        print("[DELETED] Response code 200==200")
        print(response.text)


    def test_9(self):

        url = "http://138.68.95.151:8080/rest/survey/v1/client/24078/"

        payload = "{\n\t\"clientName\": \"string1\"\n}"
        headers = {
            'accept': "application/json",
            'token': "2922f5ad-527e-4917-8561-a51a3dde58ef",
            'content-type': "application/json"
        }

        response = requests.request("PUT", url, data=payload, headers=headers)
        print("[PASSED] Response code 200==200")
        print(response.text)

if __name__ == '__main__':
    unittest.main()
