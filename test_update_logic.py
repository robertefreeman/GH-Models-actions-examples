import re
import os
from datetime import datetime

# Simulate having a panda analysis file
with open('test_panda_analysis.txt', 'w') as f:
    f.write("**Status:** Webcam Available\n**Panda Status:** Present. The panda is clearly visible in the image.\n**Activity:** The panda is chewing on bamboo")

# Read the current panda analysis
try:
    with open('test_panda_analysis.txt', 'r') as f:
        analysis = f.read().strip()
except:
    analysis = "Monitoring system active"

# Generate status summary
timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

if any(word in analysis.lower() for word in ['present', 'visible', 'panda', 'eating', 'active']):
    status_summary = f"🐼 Panda spotted! - Last updated: {timestamp}"
    status_color = "#4caf50"
elif any(word in analysis.lower() for word in ['unavailable', 'restricted', 'blocked', 'forbidden']):
    status_summary = f"📡 Webcam temporarily unavailable - Last updated: {timestamp}"  
    status_color = "#ff9800"
elif any(word in analysis.lower() for word in ['maintenance', 'down', 'error']):
    status_summary = f"🔧 Webcam under maintenance - Last updated: {timestamp}"
    status_color = "#f44336"
else:
    status_summary = f"🔄 Currently monitoring - Last updated: {timestamp}"
    status_color = "#2196f3"

print(f"✅ Status Summary: {status_summary}")
print(f"✅ Status Color: {status_color}")
print(f"✅ Analysis contains: {[word for word in ['present', 'visible', 'panda', 'eating'] if word in analysis.lower()]}")

# Clean up test file
os.remove('test_panda_analysis.txt')
