from onvif import ONVIFCamera
import time

def connect_to_camera(ip, port, user, password):
    # Connect to the camera using ONVIF
    mycam = ONVIFCamera(ip, port, user, password)
    # Create media service object
    media_service = mycam.create_media_service()
    # Get profiles
    profiles = media_service.GetProfiles()
    # Use the first profile and get token
    token = profiles[0].token
    return mycam, token

def get_camera_options():
    print("\nOptions:")
    print("1: Get Camera Information")
    print("2: Move Camera")
    print("3: Exit")
    return input("Select an option: ")

def get_camera_info(mycam):
    # Get device information
    device_info = mycam.devicemgmt.GetDeviceInformation()
    print("\nCamera Information:")
    print(f"Manufacturer: {device_info.Manufacturer}")
    print(f"Model: {device_info.Model}")
    print(f"Firmware Version: {device_info.FirmwareVersion}")
    print(f"Serial Number: {device_info.SerialNumber}")
    print(f"Hardware ID: {device_info.HardwareId}")

def move_camera(mycam, token):
    # This function needs to be implemented based on your camera's capabilities
    print("Moving camera... (functionality not implemented)")

def main():
    ip = input("Enter camera IP address: ")
    port = int(input("Enter camera port number: "))
    user = input("Enter username: ")
    password = input("Enter password: ")

    mycam, token = connect_to_camera(ip, port, user, password)

    while True:
        option = get_camera_options()

        if option == '1':
            get_camera_info(mycam)
        elif option == '2':
            move_camera(mycam, token)
        elif option == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

        time.sleep(1)

if __name__ == "__main__":
    main()