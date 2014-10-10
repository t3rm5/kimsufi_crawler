"""
kimsufi_crawler enables to manage the server availabity status in http://kimsufi.com/.
kimsufi_crawler checks the availability of an OVH Kimsufi server identified with its internal identifier
When the server status is available, the script notifies and runs a command.

Just edit the script ovh_status_loop.py and updates:

SERVER_REFERENCE = '142sk1'
CMD = 'mplayer sound.mp3'.split()

Note: one can identify the server reference in the JSON data "https://ws.ovh.com/dedicated/r2/ws.dispatcher/getAvailability2?callback=Request.JSONP.request_map.request_0"
"""

import urllib
import simplejson
import sys

URL = "https://ws.ovh.com/dedicated/r2/ws.dispatcher/getAvailability2?callback=Request.JSONP.request_map.request_0"


def is_available(server_ref, zones=None):
    """
    Get the status from the Kimsufi server reference
    Refer to page source in http://www.kimsufi.com/fr/index.xml
    For instance, Kimsufi server KS-1 has reference 142sk1 as shown in:
    <tr class="zone-dedicated-availability" data-actions="refUnavailable" data-dc="" data-ref="142sk1" data-availability="3600-">
<td><span class="blue fw800">KS-1</span></td>
    :param server_ref: Server reference
    :param zones: Not used yet
    :return: True or False
    """
    f = urllib.urlopen(URL)
    response = "".join(f.readline())
    f.close()
    # Get json
    json_rsp = response.split('Request.JSONP.request_map.request_0(', 1)[1].strip(');')
    dict_rsp = simplejson.loads(json_rsp)
    #import pprint
    #pprint.pprint(dict_rsp)
    # Select the right server data
    server_data = filter(lambda el: el['reference'] == server_ref, dict_rsp['answer']['availability'])[0]
    # If one zone is not unavailable, then the server is available
    if len(filter(lambda el: el['availability'] != 'unavailable', server_data["zones"])) > 0:
        return True
    return False


if __name__ == '__main__':
    status = is_available(sys.argv[1])
    if status:
        print "Available"
        exit(0)
    else:
        print "Unavailable"
        exit(1)
