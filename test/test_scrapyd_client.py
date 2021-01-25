# -*- coding: utf-8 -*-
from pprint import pprint

from scrapyd_api import ScrapydClient

client = ScrapydClient()
pprint(client.daemon_status())
"""
{'finished': 67,
 'node_name': 'localhost',
 'pending': 0,
 'running': 0,
 'status': 'ok',
 'total': 67}
"""