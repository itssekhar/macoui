import logging
import requests
import re

formatString = '%(asctime)s %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'
dateFmt = '%Y-%m-%d:%H:%M:%S'
logging.basicConfig(
    format=formatString,
    datefmt=dateFmt,
    level=logging.INFO,
)

requests.packages.urllib3.disable_warnings()


class MacAddress(object):
    
    def __init__(self, apikey):

        self.base_url = "https://api.macaddress.io"
        self.version = "v1"
        self.headers = {
            "X-Authentication-Token" : apikey,
            'Content-Type': 'application/json',
        }
        self.verify = False
        
        self.path = self.base_url + '/' + self.version

        self.log = logging.getLogger('macoui-lookup')

    def _get_oui(self, macaddress, output):

        resource_path = self.path
        params = {
            "output": output,
            "search": macaddress
        }

        try:
            response = requests.get(resource_path, headers=self.headers, params=params, verify=self.verify)
        except:
            self.log.exception("API request has failed. Re-try it")

        return response

    def get_oui(self, macaddress, output='json'):

        vendor_name = {
            'name': '',
        }

        valid = self.validate_mac(macaddress=macaddress)
        if not valid:
            return {}

        response = self._get_oui(macaddress=macaddress, output=output)

        if response.status_code != 200:
            response.raise_for_status()

        else:
            response_json = response.json()
            vendor_name['name'] = str(response_json['vendorDetails']['companyName'])

            if vendor_name['name'] == '':
                self.log.warning("No OUI entry exists for the given mac address")

        return vendor_name

    def validate_mac(self, macaddress):

        if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", macaddress.lower()):
            return True
        else:
            self.log.error("Invalid mac address is entered. It should be in either of these formats '44:38:39:ff:ef:57' or '44-38-39-ff-ef-57' ")
            return False

