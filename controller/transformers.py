from controller.interad_object import InteradObject


class StartappTransformer:
    def __init__(self, cid):
        self._cid = cid

    def transform(self, service):
        for i in service.data:
            if i['campaignId'] == self._cid:
                return InteradObject(imp=i["impressions"], click=i["clicks"], spent=i["spent"])


class ZeroparkTransformer:
    def __init__(self, cid):
        self._cid = cid

    def transform(self, service):
        for i in service.elements:
            if i['details']['id'] == self._cid:
                return InteradObject(imp="NA", click="NA", spent=i['stats']["spent"])

