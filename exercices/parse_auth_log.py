users, ips = {}, {}

with open("auth.log") as log_file:
    for log in log_file.readlines():
        ip, user = "", ""
        log_data = log.split('\n')[0].split(": ")[1].split(" ")
        if "Failed password" in log:
            if "message repeated" not in log:
                if "invalid user" in log:
                    ip = log_data[7]
                    user = log_data[5]
                else:
                    ip = log_data[5]
                    user = log_data[3]
        elif "Invalid user" in log:
            ip = log_data[4]
            user = log_data[2]
        ips[ip] = ips.get(ip, 0) + 1
        users[user] = users.get(user, 0) + 1

for ip, count in ips.items():
    print(f"ip: {ip} seen {count} times")
for user, count in users.items():
    print(f"user: {user} seen {count} times")