import subprocess
import getpass

# Issue on line 66 - pscp.exe (Putty Secure Copy) asks for the users password and
# I would like to handle that without prompting in the script.

def variable_confirmations(a, b):
    arg1 = a
    arg2 = b
    conf = "Is this ok? [Y/N]:\n"
    answer = input(f"The {arg1} is set to {arg2}. {conf}")
    answer = answer.upper()
    if answer == 'Y' or answer == 'YES':
        print("", end='')
        return (arg1, arg2)
    else:
        arg2 = input(f"Please type the {arg1} that you would like to use:\n")
        return variable_confirmations(arg1, arg2)


def final_confirmation(port_var, local_file_path_var, target_string):
    print(f"You are about to execute: \nC:\\installs\\pscp.exe -P {port_var} {local_file_path_var} {target_string}\n")
    answer = input("Is that ok? [Y/N] CTRL+C to cancel.")
    answer = answer.upper()
    if answer == 'Y' or answer == 'YES':
        print("", end='')
        pass
    else:
        quit()


port = "port"
port_var = "22"
port, port_var = variable_confirmations(port, port_var)

user = "username"
user_var = input("What is the username for the remote machine:\n")
user, user_var = variable_confirmations(user, user_var)

local_file_path = "local file path"
local_file_path_var = input("Drag and drop the local file that you want to send to the target machine into this window:\n")
local_file_path, local_file_path_var = variable_confirmations(local_file_path, local_file_path_var)

target_ip = "server IP address"
target_ip_var = input("What is the IP of the target machine?:\n")
target_ip, target_ip_var = variable_confirmations(target_ip, target_ip_var)

target_dir = "target directory"
target_dir_var = input("What directory do you want to drop the file in on the target machine?:\n")
target_dir, target_dir_var = variable_confirmations(target_dir, target_dir_var)

target_file_name = "target file name"
target_file_name_var = input("What do you want to name the file on the target machine?:\n")
target_file_name, target_file_name_var = variable_confirmations(target_file_name, target_file_name_var)

# Testing to see if this is even necessary
#password = ""   ONLY SET THIS ONCE OR MAKE ANOTHER FUNCTION TO TEST
#password_var = getpass.getpass(f"Please type the password for {remote_user}:\n")
#password_confirmation(a, b)

target_string = (user_var + "@" + target_ip_var + ":" + target_dir_var + target_file_name_var)

final_confirmation(port_var, local_file_path_var, target_string)

# Issue Here:
pscp_exec = subprocess.Popen([r"C:\installs\pscp.exe", "-P", port_var, local_file_path_var, target_string])
