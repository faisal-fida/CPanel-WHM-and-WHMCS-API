from handler.whm_handler import get_packages_details_categories
from handler.whmcs_handler import request


def main():
    # print("Getting server info...")
    # server_info = get_server_info(server_url)
    get_packages_details_categories()
    # print(request())
    print("Done!")


if __name__ == "__main__":
    main()
