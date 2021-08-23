import requests
import pytest

from configs.config import HOST

# 登录

def test_login():
    # url路径
    url = "https://gateway-uat2.project-g66.com/graphql?source=gibbs"

    res = requests.post(url,json={"query": query,'variables':variables1})

    print(res.request.body)
    print(res.json())

    # print("!!!!!!!")

    print(res)

    global authToken
    authToken = res.json()['data']['login']['authToken']

    print(authToken)

    if authToken == 0:
        print("failed")
    else:
        print(authToken)

        return authToken


query ="""

mutation MutationLogin($email: String!, $password: String!) {
  login(email: $email, password: $password) {
    authToken
    __typename
  }
}

"""


variables1 = {
        "email": "tina.mao@student.com",
        "password": "11111111tina"
}


# 创建booking
def test_createbooking():
    url = "https://gateway-uat2.project-g66.com/graphql?source=gibbs"

    headers = {
        "content-type": "application/json",
        "gibbs-authorization-uat2": "Bearer {authToken11}" .format(authToken11=authToken)
    }
    rsp = requests.post(url, json={"query": b_query}, headers=headers)
    print(headers)
    # print(rsp.request.body)
    # print(rsp.json())

    # bookingid = rsp.json()["data"]["createBooking"]["id"]
    # print(bookingid)

    print(rsp)


b_query = """
mutation createbooking {
  createBooking(propertyId:"eyJ0eXBlIjoiUHJvcGVydHkiLCJpZCI6Mjd9"

  input:{
    studentId:"eyJ0eXBlIjoiU3R1ZGVudCIsImlkIjoyMTR9"
    academicYearId:"eyJ0eXBlIjoiQWNhZGVtaWNZZWFyIiwiaWQiOjE3fQ=="
    tenancyOptionId:"eyJ0eXBlIjoiVGVuYW5jeU9wdGlvbiIsImlkIjoxODN9"
    tenancyStartDate:"2021-08-05"
    tenancyEndDate:"2021-11-25"
    roomTypeId:"eyJ0eXBlIjoiUm9vbVR5cGUiLCJpZCI6MjQ3fQ=="

  })
  {
    id
    bookingChainId
  }
}"""


def test_getbedsforselection():
    url = "https://gateway-uat2.project-g66.com/graphql?source=gibbs"
    headers = {
        "content-type": "application/json",
        "gibbs-authorization-uat2": "Bearer {authToken22}".format(authToken22=authToken)
    }
    rsp = requests.post(url, json={"query": s_query,'variables':variables}, headers=headers)
    print(rsp.json())
    # bookingid = rsp.json()["data"]["createBooking"]["id"]
#



s_query = """
query BedSelectQueryBeds($bookingCategory: CategoryOption, $filter: getBedsForSelectionInput!, $pageNumber: Int = 1, $pageSize: Int = 20, $propertyId: ID!) {
  getBedsForSelection(bookingCategory: $bookingCategory, filter: $filter, pageNumber: $pageNumber, pageSize: $pageSize, propertyId: $propertyId) {
    beds {
      availableNumOfBedsInFlat
      bedId
      bedName
      buildingName
      dietaryPreference
      disabilityAccess
      flat {
        id
        __typename
      }
      floorName
      genderPreference
      petPreference
      smokingPreference
      totalNumOfBedsInFlat
      __typename
    }
    pageNumber
    pageSize
    total
    totalPage
    __typename
  }
}



"""


variables = {

  "pageNumber": 1,
  "pageSize": 20,
  "propertyId": "eyJ0eXBlIjoiUHJvcGVydHkiLCJpZCI6Mjd9",
  "bookingCategory": "DIRECT_LET",
  "filter": {
    "roomTypeId": "eyJ0eXBlIjoiUm9vbVR5cGUiLCJpZCI6MjQ3fQ==",
    "tenancyOptionId": "eyJ0eXBlIjoiVGVuYW5jeU9wdGlvbiIsImlkIjoxODN9",
    "tenancyStartDate": "2021-08-05",
    "tenancyEndDate": "2021-11-25",
    "intervalForTurnaround": 0
  }
}
