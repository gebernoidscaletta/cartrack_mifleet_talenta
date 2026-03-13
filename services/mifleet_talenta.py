import requests
import time
import threading
from logging import log

from typing import List, Tuple, Any, Dict

from constants.constantsEndpoint import ConstantsEndpoint
from data.model.hmacHeadersData import HmacHeadersData
from data.request.getReimburseData import GetReimburseData
from data.request.updateFuel import UpdateFuel
from data.request.updateToll import UpdateToll
from data.response.responseFuel import ResponseFuel
from data.response.responseToll import ResponseToll
from data.response.responseReimburseData import ResponseReimburseData
from enumeration.mifleetEnum import ModuleName
from util import utilAuth
from datetime import datetime, timedelta
from constants.constantsGeneral import ConstantsGeneral
from util.utilLogger import Log

log = Log()


def servicesMifleetTalenta(currTime: str, endTime: str) -> bool | None:
    try:
        log.info("Starting to get data from Talenta")
        log.info(f"Current Time: {currTime}, End Time: {endTime}")

        dataRaw = getDataFromTalenta(currTime, endTime)
        log.info(f"Data : {dataRaw}")

        # getReimbursementData : List[Dict[str, Any]] = getDataFromTalenta(currTime, endTime)
        # log.info(f"Data : {getReimbursementData}")
        #
        # listReimburseData : List[GetReimburseData] = [GetReimburseData(**item) for item in getReimbursementData]
        #
        # for count, item in enumerate(listReimburseData):
        #     try :
        #         logAllItems(count, item)
        #         #TODO : add logic for check data for each sub module in cartrack mifleet (fuel and tolls) and map to each sub module in cartrack mifleet (fuel and tolls)
        #         talentaResponse: GetReimburseData = parsingDataFromTalenta(item)
        #
        #         log.info(f"Sub-Module Status : Fuel")
        #         if talentaResponse.module_name == ModuleName.FUEL:
        #             fuelRequest: UpdateFuel = mapDataToFuel(talentaResponse)
        #             responseFuel: ResponseFuel = servicesMifleetFuel(fuelRequest)
        #             log.info(f"Response Fuel : {responseFuel}")
        #         elif talentaResponse.module_name == ModuleName.TOLL:
        #             tollRequest: UpdateToll = mapDataToToll(talentaResponse)
        #             responseToll: ResponseToll = servicesMifleetToll(tollRequest)
        #             log.info(f"Response Toll : {responseToll}")
        #         else :
        #             log.error(f"Unknown Module Name : {talentaResponse.module_name}")
        #
        #     except Exception as e:
        #         log.error(f"Error Processing Item {count} with id {item.id} : {e}")

    except Exception as e:
        log.error(f"Error Processing : {e}")
        return False


# TODO : Add logic for looping each pagination
def getDataFromTalenta(currTime: str, endTime: str):
    responseData = []
    params: GetReimburseData = GetReimburseData(
        start_request_date=currTime,
        end_request_date=endTime
    )
    hmacData = HmacHeadersData(
        url=f"{ConstantsGeneral.getTalentaProductionBaseUrl()}{ConstantsEndpoint.TALENTA.REIMBURSEMENT_V3}",
        method="GET",
        hmac_username=ConstantsGeneral.getTalentaHmacUsername(),
        hmac_secret=ConstantsGeneral.getTalentaHmacSecret(),
        params=params.toQueryParams()
    )
    currentPage = 1
    while True:
        params.page = currentPage
        response = requests.get(
            url=f"{ConstantsGeneral.getTalentaProductionBaseUrl()+ConstantsEndpoint.getTalentaReimbursementV3()}",
            params=params.toQueryParams(),
            headers=utilAuth.hmacHeadersGenerator(hmacData)
        )
        log.info(f"Request Full URL : {response.url}")
        response.raise_for_status()
        if response.status_code == 200:
            body = response.json()
            data = body.get("data", {})

            reimbursements = data.get("reimbursement", [])
            pagination = data.get("pagination", {})

            log.info(f"Current Page : {currentPage}")
            log.info(f"Last Page : {pagination.get('last_page')}")

            responseData.extend(reimbursements)

            if currentPage >= pagination.get("last_page", 1):
                log.info("All Data Successfully Fetched")
                break

            currentPage += 1

    log.info(f"Successfully got data from Talenta")
    return responseData


def parsingDataFromTalenta(response: GetReimburseData) -> GetReimburseData:
    a = a
    #TODO : parsing data from talenta and map to each sub module in cartrack Mifleet (fuel and tolls)


def mapDataToFuel() -> UpdateFuel:
    a = a
    #TODO : mapping data from talenta to fuel module in cartrack mifleet


def mapDataToToll() -> UpdateToll:
    a = a
    #TODO : mapping data from talenta to toll module in cartrack mifleet


#TODO : Is this required?
def logAllItems(count, item):
    log.info(f"Item No : {count}")
    log.info(f"Id : {item.id} ")
    log.info(f"Transaction Id : {item.transaction_id} ")
    log.info(f"Reimbursement Id : {item.reimbursement_id} ")
    log.info(f"Reimbursement Name : {item.reimbursement_name} ")
    log.info(f"Request Date : {item.request_date} ")
    log.info(f"Approved Date : {item.approved_date} ")
    log.info(f"Status : {item.status} ")
    log.info(f"Request Amount : {item.request_amount} ")
    log.info(f"Paid Amount : {item.paid_amount} ")
    log.info(f"Description : {item.description} ")
    log.info(f"Created At : {item.created_at} ")


def scheduler():
    log.info("Scheduler started")
    startTime = datetime.now()
    # time.sleep(864000)

    while True:
        endTime = datetime.now()
        # startTimeStr = startTime.strftime("%Y-%m-%d")
        # endTimeStr = endTime.strftime("%Y-%m-%d")
        startTimeStr = "2026-03-01"
        endTimeStr = "2026-03-10"
        isSuccess: bool = servicesMifleetTalenta(startTimeStr, endTimeStr)
        startTime = endTime if isSuccess else startTime

        time.sleep(864000)


if __name__ == "__main__":
    log.info("Start Mifleet Talenta Service")
    thread = threading.Thread(target=scheduler)
    thread.daemon = True
    thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log.info("Stopping Mifleet Talenta Service")
