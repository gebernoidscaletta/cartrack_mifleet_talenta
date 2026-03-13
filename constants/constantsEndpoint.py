class ConstantsEndpoint:
    _MIFLEET_FUEL = "/mifleet/fuel"
    _MIFLEET_TOLL = "/mifleet/toll"
    _TALENTA_REIMBURSEMENT_V3 = "/v2/talenta/v3/reimbursement"
    
    @staticmethod
    def getMifleetFuel():
        return ConstantsEndpoint._MIFLEET_FUEL
    
    @staticmethod
    def getMifleetToll():
        return ConstantsEndpoint._MIFLEET_TOLL
    
    @staticmethod
    def getTalentaReimbursementV3():
        return ConstantsEndpoint._TALENTA_REIMBURSEMENT_V3

    class TALENTA:
        REIMBURSEMENT_LIST = "v2/talenta/v2/reimbursement/list"
        REIMBURSEMENT_V3 = "/v2/talenta/v3/reimbursement"

    class MIFLEET:
        FUEL = "/mifleet/fuel"
        TOLL = "/mifleet/toll"
    