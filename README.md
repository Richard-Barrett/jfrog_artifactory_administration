# jfrog_artifactory_administration

Python Scripts for JFrog Artifactory Administration and Data Tasks

- [Scripts](https://github.com/Richard-Barrett/jfrog_artifactory_administration/tree/main/scripts) - The directory to hold one-off python scripts for interacting with Artifactory.

## Overview

This repository is dedicated to helping users pull out data and/or run administrative tasks to JFrog Artifactory.
One of the limiting factors of the Artifactory console is that there is no way to pull down users as a csv or into a an excel file. 
If your manager asks for this, there is no method in the console UI to achieve this. 
Therefore, run these scripts to pull down users.

You must have three enivornmental variables exported out in your terminal for the scripts to be successful:

- ARTIFACTORY_ADMIN_USER
- ARTIFACTORY_TARGET_URL 
- ARTIFACTORY_ADMIN_API_KEY

NOTE: THE ARTIFACTORY_TARGET_URL NEEDS TO ADHERE TO THE FOLLOWING `https://<YOUR_SERVER_FQDN>/artifactory/api/security/users`

You can export the variables in your terminal prompt as follows:

```bash
export ARTIFACTORY_TARGET_URL="https://<YOUR_SERVER_FQDN>/artifactory/api/security/users"
```

replace `<YOUR_SERVER_FQDN>` with the correct URL matching your artifactory server.

SPECIAL NOTE: `"https://<YOUR_SERVER_FQDN>/artifactory/api/security/users"` seems to work only for Artifactory on-prem versions and not the SaaS version.

## Usage

```bash
python3 scripts/get_users_list.py
python3 scripts/get_users_details.py
```

After running the scripts, it will produce and write out to a `.csv` file in your local directory.

## Limitations

NOTE: ONLY WORKS ON MACOS OR LINUX
