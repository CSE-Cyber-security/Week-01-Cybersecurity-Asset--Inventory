import json
import os

DATA_FILE = "data_assets.json"


# Load assets from JSON file
def load_assets():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (json.JSONDecodeError, OSError):
        return []


# Save assets to JSON file
def save_assets(assets):
    with open(DATA_FILE, "w") as file:
        json.dump(assets, file, indent=4)


# Display one asset
def display_asset(asset):
    print("\n----------------------------------------")
    print("Asset ID         :", asset.get("id", ""))
    print("Asset Name       :", asset.get("name", ""))
    print("Asset Type       :", asset.get("type", ""))
    print("IP Address       :", asset.get("ip_address", ""))
    print("Department       :", asset.get("department", ""))
    print("Operating System :", asset.get("operating_system", ""))
    print("Risk Level       :", asset.get("risk_level", ""))
    print("Security Level   :", asset.get("security_level", ""))
    print("----------------------------------------")


# 1. ADD ASSET
def add_asset():
    assets = load_assets()

    print("\n--- Add Asset ---")

    asset_id = input("Enter Asset ID: ").strip()

    if not asset_id:
        print("Asset ID cannot be empty.")
        return

    for asset in assets:
        if str(asset.get("id", "")).lower() == asset_id.lower():
            print("Asset ID already exists.")
            return

    name = input("Enter Asset Name: ").strip()
    asset_type = input("Enter Asset Type: ").strip()
    ip_address = input("Enter IP Address: ").strip()
    department = input("Enter Department: ").strip()
    operating_system = input("Enter Operating System: ").strip()
    risk_level = input("Enter Risk Level: ").strip()
    security_level = input("Enter Security Level: ").strip()

    new_asset = {
        "id": asset_id,
        "name": name,
        "type": asset_type,
        "ip_address": ip_address,
        "department": department,
        "operating_system": operating_system,
        "risk_level": risk_level,
        "security_level": security_level
    }

    assets.append(new_asset)
    save_assets(assets)

    print("Asset added successfully.")


# 2. VIEW ASSETS
def view_assets():
    assets = load_assets()

    print("\n--- View Assets ---")

    if not assets:
        print("No assets found.")
        return

    for asset in assets:
        display_asset(asset)


# 3. UPDATE ASSET
def update_asset():
    assets = load_assets()

    print("\n--- Update Asset ---")

    asset_id = input("Enter Asset ID to update: ").strip()

    for asset in assets:
        if str(asset.get("id", "")).lower() == asset_id.lower():

            print("\nEnter new values.")
            print("Press Enter to keep the existing value.")

            name = input(
                f"Asset Name [{asset.get('name', '')}]: "
            ).strip()

            asset_type = input(
                f"Asset Type [{asset.get('type', '')}]: "
            ).strip()

            ip_address = input(
                f"IP Address [{asset.get('ip_address', '')}]: "
            ).strip()

            department = input(
                f"Department [{asset.get('department', '')}]: "
            ).strip()

            operating_system = input(
                f"Operating System [{asset.get('operating_system', '')}]: "
            ).strip()

            risk_level = input(
                f"Risk Level [{asset.get('risk_level', '')}]: "
            ).strip()

            security_level = input(
                f"Security Level [{asset.get('security_level', '')}]: "
            ).strip()

            if name:
                asset["name"] = name

            if asset_type:
                asset["type"] = asset_type

            if ip_address:
                asset["ip_address"] = ip_address

            if department:
                asset["department"] = department

            if operating_system:
                asset["operating_system"] = operating_system

            if risk_level:
                asset["risk_level"] = risk_level

            if security_level:
                asset["security_level"] = security_level

            save_assets(assets)

            print("Asset updated successfully.")
            return

    print("Asset not found.")


# 4. DELETE ASSET
def delete_asset():
    assets = load_assets()

    print("\n--- Delete Asset ---")

    asset_id = input("Enter Asset ID to delete: ").strip()

    for asset in assets:
        if str(asset.get("id", "")).lower() == asset_id.lower():

            assets.remove(asset)
            save_assets(assets)

            print("Asset deleted successfully.")
            return

    print("Asset not found.")


# 5. SEARCH ASSET
def search_asset():
    assets = load_assets()

    print("\n--- Search Asset ---")

    keyword = input(
        "Enter Asset ID or Asset Name to search: "
    ).strip().lower()

    if not keyword:
        print("Search value cannot be empty.")
        return

    found = False

    for asset in assets:
        asset_id = str(asset.get("id", "")).lower()
        asset_name = str(asset.get("name", "")).lower()

        if keyword in asset_id or keyword in asset_name:
            display_asset(asset)
            found = True

    if not found:
        print("Asset not found.")


# MAIN MENU
def main():
    while True:
        print("\n==========================================")
        print("     CYBERSECURITY ASSET INVENTORY")
        print("==========================================")
        print("1. Add Asset")
        print("2. View Assets")
        print("3. Update Asset")
        print("4. Delete Asset")
        print("5. Search Asset")
        print("6. Exit")
        print("==========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_asset()

        elif choice == "2":
            view_assets()

        elif choice == "3":
            update_asset()

        elif choice == "4":
            delete_asset()

        elif choice == "5":
            search_asset()

        elif choice == "6":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please enter 1 to 6.")


if __name__ == "__main__":
    main()
