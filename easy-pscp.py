import subprocess
import getpass

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

words=["port", "username", "local file path", "server IP address", "target directory", "target file name"]
port_var = "22"
user_var = input("What is the username for the remote machine:\n")
local_file_path_var = input("Drag and drop the local file that you want to send to the target machine into this window:\n")
target_ip_var = input("What is the IP of the target machine?:\n")
target_dir_var = input("What directory do you want to drop the file in on the target machine?:\n")
target_file_name_var = input("What do you want to name the file on the target machine?:\n")

port, port_var = variable_confirmations(words[0], port_var)
user, user_var = variable_confirmations(words[1], user_var)
local_file_path, local_file_path_var = variable_confirmations(words[2], local_file_path_var)
target_ip, target_ip_var = variable_confirmations(words[3], target_ip_var)
target_dir, target_dir_var = variable_confirmations(words[4], target_dir_var)
target_file_name, target_file_name_var = variable_confirmations(words[5], target_file_name_var)

password_var = getpass.getpass(f"Please type the password for {user_var}:\n")
target_string = (user_var + "@" + target_ip_var + ":" + target_dir_var + target_file_name_var)
final_confirmation(port_var, local_file_path_var, target_string)
pscp_exec = subprocess.Popen([r"C:\installs\pscp.exe", "-P", port_var, "-pw", password_var, local_file_path_var, target_string])
