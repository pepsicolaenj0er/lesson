logs = [
    "192.168.0.1",
    "192.168.0.2",
    "192.168.0.3",
    "192.168.0.1",
    "192.168.0.2",
    "192.168.0.1",
    "192.168.0.4",
    "192.168.0.2",
    "192.168.0.5",
    "192.168.0.2",
    "192.168.0.3",
]
ipCounts = {}
for ip in logs:
    if ip in ipCounts: 
        ipCounts[ip]+=1 
    else:
        ipCounts[ip]=1

sortedIp = sorted(ipCounts.items(), key=lambda x: x[1],reverse=True)
top_3 = sortedIp[:3]
print("топ 3 по активности")
for ip, count in top_3:
    print(f"{ip} --> {count} раза")

