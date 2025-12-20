import json

from src.pysysinfo.dumps.mac.mac_dump import MacHardwareManager
import time

start_time = time.time()
lhm = MacHardwareManager()

lhm.fetch_cpu_info()
lhm.fetch_memory_info()
lhm.fetch_storage_info()
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

json_data = json.loads(lhm.info.model_dump_json())

with open("response.json", "w") as f:
    json.dump(json_data, f, indent=2)

print(json.dumps(json_data, indent=2))
# print("done")