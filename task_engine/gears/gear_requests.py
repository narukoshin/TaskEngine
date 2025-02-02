from task_engine.gears import Gear, GearError
import requests
from typing import Union

class GearRequestsGet(Gear):
    def __init__(self) -> None:
        super().__init__()
        self._gear_name = "Requests GET gear"
        self._gear_version = "1.0"
    
    def _execute(self, params: dict) -> Union[dict, GearError]:
        if 'requests_url' not in params:
            return self.error("'requests_url' param not in params.")
        requests_obj = requests.get(params['requests_url'])

        new_params = params
        new_params.update({
            'requests_object': requests_obj,
            'requests_code': requests_obj.status_code
        })
        return new_params