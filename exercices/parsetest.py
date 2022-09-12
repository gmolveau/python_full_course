log_failed_password = "Mar 29 14:15:41 ip-10-77-20-248 sshd[2414]: Failed password for invalid user pi from 181.25.206.27 port 50378 ssh2"
log_data = log_failed_password.split(" ")
ip = log_data[12]
user = log_data[9]
