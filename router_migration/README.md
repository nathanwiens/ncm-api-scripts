# Cradlepoint Router Migration Tool
This is an NCM API scipt that copies router level configuration from one router to another. 
As the NCM API cannot access encrypted fields, this script doesn't copy any of them.

This script will not copy groups or group-level configuration.

INSTALL AND RUN INSTRUCTIONS

1. Edit the config.py file with you Account ID and NCM API Keys.

2. Install requirements.
    ```
    pip3 install -r requirements.txt
    ```

3. Edit the Router_Migration.xlsx file with the source and destination router IDs. 
   Ensure that Column C is blank for all rows. 

4. Run the script.
    ```
    python3 router_migration.py
    ```
