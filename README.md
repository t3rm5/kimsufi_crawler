kimsufi_crawler
===============

kimsufi_crawler enables to manage the server availabity status in http://kimsufi.com/.
kimsufi_crawler checks the availability of an OVH Kimsufi server identified with its internal identifier
When the server status is available, the script notifies and runs a command.

Just edit the script ovh_status_loop.py and updates:

SERVER_REFERENCE = '142sk1'
CMD = 'mplayer sound.mp3'.split()

Note: one can identify the server reference in the JSON data "https://ws.ovh.com/dedicated/r2/ws.dispatcher/getAvailability2?callback=Request.JSONP.request_map.request_0"

How to run:
python ovh_get_avail_status.py 
