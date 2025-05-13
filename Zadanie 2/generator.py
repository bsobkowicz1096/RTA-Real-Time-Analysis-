import json, os, random, time
from datetime import datetime, timedelta

output_dir = "data/stream"
os.makedirs(output_dir, exist_ok=True)

event_types = ["view", "cart", "purchase"]
categories = ["electronics", "books", "fashion", "home", "sports"]

def generate_event():
    return {
        "user_id": f"u{random.randint(1, 50)}",
        "event_type": random.choices(event_types, weights=[0.6, 0.25, 0.15])[0],
        "timestamp": (datetime.utcnow() - timedelta(seconds=random.randint(0, 300))).isoformat(),
        "product_id": f"p{random.randint(100, 120)}",
        "category": random.choice(categories),
        "price": round(random.uniform(10, 1000), 2)
    }

# Simulate file-based streaming
while True:
    batch = [generate_event() for _ in range(50)]
    filename = f"{output_dir}/events_{int(time.time())}.json"
    with open(filename, "w") as f:
        for e in batch:
            f.write(json.dumps(e) + "\n")
    print(f"Wrote: {filename}")
    time.sleep(5)