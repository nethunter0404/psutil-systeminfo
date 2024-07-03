import psutil

# Mantıksal CPU sayısı 
logical_cpu_count = psutil.cpu_count(logical=True)
print("mantiksal cpu ", logical_cpu_count)
# Fiziksel CPU sayısı 
physical_cpu_count = psutil.cpu_count(logical=False)
print("fiziksel cpu : " , physical_cpu_count)


# Anlık CPU kullanım yüzdesi
cpu_usage_for_moment = psutil.cpu_percent(interval=1)
print("cpu usage",cpu_usage_for_moment)


# Her bir çekirdeği ele alalım 
cpu_usage_loop = psutil.cpu_percent(interval=1,percpu=True)
for i, cpu in  enumerate(cpu_usage_loop):
    print(f"çekirdek{i}=cpu:{cpu}")
    
    
# Genel CPU kullanimini görmek .
cpu_usage_5 = psutil.cpu_percent(interval=0)
print(f"Genel CPU Kullanımı: {cpu_usage_5}%") 


# sanal bellek kullanimi 
virtual_memory = psutil.virtual_memory()
print("virtual memory : " , virtual_memory  )
    

# disk kullanimi 
disk_usage = psutil.disk_usage("/")
print(f"disk usage : {disk_usage}")


# ağ giriş ve çıkışları öğrenelim. 
net_io_counts = psutil.net_io_counters()
print(f"net io counter : {net_io_counts}")

# network bağlantıları 
network_connections = psutil.net_connections()
print(f"network connections : {network_connections}")


# sistem bilgileri 
boot_time = psutil.boot_time()
print(f"boot time {boot_time}")


# anlık çalışan process'ler 
process = [proc.info for proc in psutil.process_iter(["pid","name"])]
print(f"process : {process}")