class ConstantsGeneral:
    _CARTRACK_API_USERNAME = ""
    _CARTRACK_API_PASSWORD = ""
    _TALENTA_HMAC_USERNAME = ""
    _TALENTA_HMAC_SECRET = ""
    _CARTRACK_INDONESIA_BASE_URL = "https://fleetapi-id.cartrack.com/rest"
    _TALENTA_DEVELOPMENT_BASE_URL = "https://sandbox-api.mekari.com"
    _TALENTA_PRODUCTION_BASE_URL = "https://api.mekari.com"
    
    @staticmethod
    def getCartrackApiUsername():
        return ConstantsGeneral._CARTRACK_API_USERNAME
    
    @staticmethod
    def getCartrackApiPassword():
        return ConstantsGeneral._CARTRACK_API_PASSWORD
    
    @staticmethod
    def getTalentaHmacUsername():
        return ConstantsGeneral._TALENTA_HMAC_USERNAME
    
    @staticmethod
    def getTalentaHmacSecret():
        return ConstantsGeneral._TALENTA_HMAC_SECRET
    
    @staticmethod
    def getCartrackIndonesiaBaseUrl():
        return ConstantsGeneral._CARTRACK_INDONESIA_BASE_URL
    
    @staticmethod
    def getTalentaDevelopmentBaseUrl():
        return ConstantsGeneral._TALENTA_DEVELOPMENT_BASE_URL
    
    @staticmethod
    def getTalentaProductionBaseUrl():
        return ConstantsGeneral._TALENTA_PRODUCTION_BASE_URL