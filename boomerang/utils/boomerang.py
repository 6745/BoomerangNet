from flask import Flask, render_template
from flask_restful import Api
import argparse
import os

# Import the services
from boomerang.services.routes.routestatics import routeStatics
from boomerang.services.routes.machineroutes import machineRoutes
from boomerang.services.routes.ranking import routeRanking
from boomerang.services.routes.notice import routeNotices
from boomerang.services.routes.auth import routeAuth

app = Flask(__name__, template_folder=os.path.abspath('./boomerang/web/templates'))
api = Api(app)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/services')
def services():
    return "If you're reading this, services are OK!"

# Start using the imports
api.add_resource(routeStatics.routeEmergency, '/services/Emergency.txt')
api.add_resource(routeStatics.routeNewSongEvent, '/services/newsongevent.txt')
api.add_resource(machineRoutes.routeMachinePoints, '/services/games/gameCenters/points/machine/<string:machine_id>')
api.add_resource(routeRanking.bootupRanking, '/services/games/bestRankings')
api.add_resource(routeNotices, '/services/games/notices')
api.add_resource(routeAuth.noCardLogin, '/services/auth/noCardLogin')

def main() -> None:
    parser = argparse.ArgumentParser(description="BoomerangNet: A 3rd party network for Beatcraft Cyclon, written in Flask.")
    parser.add_argument("-p", "--port", help="Port to listen on. Defaults to 80", type=int, default=80)
    args = parser.parse_args()

    # Run the app
    app.run(host='0.0.0.0', port=args.port, debug=True)

if __name__ == '__main__':
    main()