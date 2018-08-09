import subprocess

def user_confirmation(file_to_send, remote_user, remote_ip, remote_string, remote_dir, file_name):
    print(f"You are about to execute: \nC:\\installs\\pscp.exe -P 22 -pw REDACTED {file_to_send} {remote_string}\n")
    answer = input("Is that ok? [Y/N] CTRL+C to cancel.")
    answer = answer.upper()
    if answer == 'Y' or answer == 'YES':
        return (remote_ip, remote_dir)
        print("", end='')
    else:
        answer = input(f"Remote machines IP is set to {remote_ip}. Is that ok? [Y/N]")
        answer = answer.upper()
        if answer == 'Y' or answer == 'YES':
            print("", end='')
        else:
            remote_ip = input("What is the IP of the remote machine?:\n")
        answer = input(f"The file will be dropped in {remote_dir}. Is that ok? [Y/N]")
        answer = answer.upper()
        if answer == 'Y' or answer == 'YES':
            print("", end='')
        else:
            remote_dir = input("What directory do you want to put the file in?:\n")
    remote_string = (remote_user + "@" + remote_ip + ":" + remote_dir + file_name)
    user_confirmation(file_to_send, remote_user, remote_ip, remote_string, remote_dir, file_name)

port = "22"
password = "password"
file_to_send = input("Drag and drop the file into this terminal, then press enter:\n")
remote_user = "codeutility" #print("Username is set in the script to 'codeutility'")
remote_ip = "192.168.1.92" #input("What is the IP of the remote Box?")
remote_dir = "/home/codeutility/" #input("What directory do you want to drop the file in?:\n")
file_name = input("What do you want to name the file on the remote machine?:\n")
remote_string = (remote_user + "@" + remote_ip + ":" + remote_dir + file_name) # Dont fuck with this

user_confirmation(file_to_send, remote_user, remote_ip, remote_string, remote_dir, file_name)
subprocess.Popen([r"C:\installs\pscp.exe", "-P", port, "-pw", password, file_to_send, remote_string])
