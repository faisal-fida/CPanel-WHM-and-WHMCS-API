import dotenv, os

dotenv.load_dotenv()
whmcs_secret = os.getenv("WHMCS_SECRET")
whmcs_identifier = os.getenv("WHMCS_IDENTIFIER")
whm_auth_headers = os.getenv("WHM_AUTH_HEADERS")
whm_server_url = os.getenv("WHM_SERVER_URL")

whm_headers = {
    "Authorization": whm_auth_headers,
}
whm_params = {
    "api.version": "1",
}


whm_packages_shared = [
    "beewebh1_shared1",
    "beewebh1_shared2",
    "beewebh1_shared3",
    "beewebh1_shared4",
]

whm_packages_student = [
    "beewebh1_student",
]

whm_packages_u = [
    "beewebh1_u1",
    "beewebh1_u2",
    "beewebh1_u3",
]

whm_packages_web = [
    "beewebh1_web_1",
    "beewebh1_web_2",
    "beewebh1_web_3",
    "beewebh1_web_4",
]

whm_initial_columns = [
    "pkg_name",
    "QUOTA",
    "BWLIMIT",
    "MAXPOP",
    "MAXSUB",
    "MAXADDON",
]

whm_columns_names = [
    "Packages",
    "Disk Space",
    "Monthly Transfer (Bandwidth)",
    "Email Accounts",
    "Sub-Domains",
    "Sites",
]

whmcs_payload = {
    "action": "GetProducts",
    "username": whmcs_identifier,
    "password": whmcs_secret,
    "pid": "46,47,48,50,52,53,54,55,56,57,58",
    "responsetype": "json",
}


def get_whm_vriables():
    return {
        "whm_server_url": whm_server_url,
        "whm_headers": whm_headers,
        "whm_params": whm_params,
        "whm_packages_shared": whm_packages_shared,
        "whm_packages_web": whm_packages_web,
        "whm_packages_u": whm_packages_u,
        "whm_packages_student": whm_packages_student,
        "whm_initial_columns": whm_initial_columns,
        "whm_columns_names": whm_columns_names,
    }


def get_whmcs_variables():
    return {
        "payload": whmcs_payload,
    }
