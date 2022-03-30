"""
Cradlepoint NCM API Router Migration Tool
Created by Nathan Wiens (nathan.wiens@cradlepoint.com)

config.py

Change the account_id value to your NCM Account ID
Change the api_keys dictionary to match your NCM API Keys
Set DEBUG = True if you want verbose configuration output for debugging.

"""

DEBUG = True

account_id = 12345

EXCEL_FILE = 'Router_Migration.xlsx'

# NCM API Keys
api_keys = {
    'X-CP-API-ID': 'AAAAAAAAAAAAAAAAAAAAAAAAA',
    'X-CP-API-KEY': 'BBBBBBBBBBBBBBBBBBBBBBBBB',
    'X-ECM-API-ID': 'CCCCCCCCCCCCCCCCCCCCCCCCC',
    'X-ECM-API-KEY': 'DDDDDDDDDDDDDDDDDDDDDDDDD'
}
