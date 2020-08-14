# org-and-space-mgmt

This project is used to move the databases from one foundation to another.  

** The plan
1.  Write code which generates the commands to move the data bases.  The list of databases must be provided.
1.  Write code which generates list of potential databases given a list of TBD.
1.  Write code which generates the commands which set and stores the service IDs.
1.  Write code which generates the commands which set and stores the SSO credentials.
1.  Write code which executes the commands which were generated by the previous stages.

** Manifest

- `utils.py`---general utilities
- `cf_utils.py`---utilities to make `cf curl` calls.

** To-Do

** STATUS

- 13 Aug 2020
  - Started to transcribe code.
  - Started to review Python reference manual.

- 14 Aug 2020
  - Finished the outline of `utils.py`.
