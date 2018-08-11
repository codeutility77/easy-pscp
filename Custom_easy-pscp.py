import subprocess
import getpass

def final_confirmation(port_var, local_file_path_var, target_string):
    print(f"You are about to execute: \nC:\\installs\\pscp.exe -P {port_var} {local_file_path_var} {target_string}\n")
    answer = input("Is that ok? [Y/N] CTRL+C to cancel.")
    answer = answer.upper()
    if answer == 'Y' or answer == 'YES':
        print("", end='')
        pass
    else:
        quit()

words=["port", "username", "local file path", "server IP address", "target directory", "target file name"]
port_var = "22"
user_var = "Type_Your_Username_Here"
local_file_path_var = input("Drag and drop the local file that you want to send to the target machine into this window:\n")
target_ip_var = "Type_The_REMOTE_Machines_IP_Here"
target_dir_var = (f"/home/{user_var}/")  # Change this to the path you use the most for convinience
target_file_name_var = input("What do you want to name the file on the target machine?:\n")

password_var = getpass.getpass(f"Please type the password for {user_var}:\n")
target_string = (user_var + "@" + target_ip_var + ":" + target_dir_var + target_file_name_var)
final_confirmation(port_var, local_file_path_var, target_string)
pscp_exec = subprocess.Popen([r"Paste_the_path_to_pscp.exe_Here", "-P", port_var, "-pw", password_var, local_file_path_var, target_string])
