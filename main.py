from my_lib import *
import json
#print(agents.get_my_agent()['data'])
#print(contracts.get_contracts()['data'])
#print(ships.get_ships()['data'])
#results = systems.get_waypoint_by_tag("X1-VC79", "SHIPYARD")


results = ships.get_ships()
for result in results:
    print(json.dumps(result, indent=4))
    input("Press Enter to Continue")

#print(len(results))