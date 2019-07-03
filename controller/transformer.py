class Transformer:
    def __init__(self, cid):
        self._cid = cid

    def transform_startapp_data(self, service):
        return_data = {}
        for i in service.data:
            if i['campaignId'] == self._cid:
                return_data.update({"impressions": i["impressions"], "clicks": i["clicks"], "spent": i["spent"]})
        return return_data

    def transform_zeropark_data(self, service):
        return_data = {}
        for i in service.elements:
            if i['details']['id'] == self._cid:
                return_data.update({"impressions": "NA", "clicks": "NA", "spent": i['stats']["spent"]})
        return return_data

