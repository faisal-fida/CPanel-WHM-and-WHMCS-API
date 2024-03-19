import requests
import pandas as pd
from handler.variable_handler import get_whm_vriables

whm_variables = get_whm_vriables()

server_url = whm_variables["whm_server_url"]
headers = whm_variables["whm_headers"]
params = whm_variables["whm_params"]
package_names_shared = whm_variables["whm_packages_shared"]
package_names_web = whm_variables["whm_packages_web"]
package_names_u = whm_variables["whm_packages_u"]
package_names_student = whm_variables["whm_packages_student"]
initial_columns = whm_variables["whm_initial_columns"]
columns_names = whm_variables["whm_columns_names"]


def request(server_url, params):
    response = requests.get(server_url, params=params, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}")
    return response.json()


def get_package_info(pkg_name):
    params["pkg"] = pkg_name
    return request(server_url + "getpkginfo/", params)["data"]["pkg"]


def save_packages_to_csv(packages, pkg_name):
    df = pd.json_normalize(packages)
    df = df[initial_columns]
    df.columns = columns_names
    df = df.fillna("Unlimited")
    df = df.transpose()
    if "beewebh1_shared" in pkg_name:
        filename = "Shared Packages"
    elif "beewebh1_web" in pkg_name:
        filename = "Wordpress Packages"
    elif "beewebh1_u" in pkg_name:
        filename = "Cloud Packages"
    elif "beewebh1_student" in pkg_name:
        filename = "Student Packages"
    print(f"Saving {filename}...")
    df.to_csv(f"output/{filename}.csv", header=False)


def get_packages_details(package_names):
    packages = []
    package_names_map = {
        "package_names_web": [
            "StartUp",
            "Plus",
            "Professional",
            "Business",
        ],
        "package_names_u": [
            "Plus",
            "Choice Plus",
        ],
        "package_names_student": [
            "Student",
        ],
        "default": [
            "StartUp",
            "Plus",
            "Professional",
            "Business",
        ],
    }

    for pkg_name in package_names:
        package_info = get_package_info(pkg_name)
        new_packages_names = package_names_map.get(
            pkg_name, package_names_map["default"]
        )
        package_info["pkg_name"] = new_packages_names[package_names.index(pkg_name)]
        # print(f"Getting {pkg_name} info...", end="\r")
        packages.append(package_info)

    save_packages_to_csv(packages, pkg_name)


def get_packages_details_categories():
    get_packages_details(package_names_shared)
    get_packages_details(package_names_web)
    get_packages_details(package_names_u)
    get_packages_details(package_names_student)


def create_package(pkg_name, pkg_info):
    # params["name"] = pkg_name
    # params["quota"] = pkg_info["QUOTA"]
    # params["bwlimit"] = pkg_info["BWLIMIT"]
    # params["maxpop"] = pkg_info["MAXPOP"]
    # params["maxsql"] = pkg_info["MAXSQL"]
    # params["maxsub"] = pkg_info["MAXSUB"]
    # params["maxpark"] = pkg_info["MAXPARK"]
    # params["maxaddon"] = pkg_info["MAXADDON"]
    # params["max_emailacct_quota"] = pkg_info["MAX_EMAILACCT_QUOTA"]
    # return request(server_url + "addpkg/", params)
    pass
