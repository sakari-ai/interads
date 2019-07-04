from flask import Flask
from flask_restful import Api

from controller.campaign_stats_endpoint import CampaignStatsResource

app = Flask(__name__)
api = Api(app)

api.add_resource(CampaignStatsResource, '/stats/<string:source>')

if __name__ == "__main__":
    app.run(debug=True)