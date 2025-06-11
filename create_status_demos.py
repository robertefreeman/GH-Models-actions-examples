#!/usr/bin/env python3
"""
Create example status images to demonstrate the enhanced panda cam system
"""

import subprocess
import time

def create_demo_image(status_type, description):
    """Create a demo status image"""
    current_time = time.strftime("%H:%M UTC", time.gmtime())
    
    status_configs = {
        "unavailable": {
            "text": f"🐼 Panda Cam\\nTemporarily\\nUnavailable\\n\\n(Access restricted)\\n{current_time}",
            "bg_color": "lightblue",
            "text_color": "darkblue"
        },
        "accessible": {
            "text": f"🐼 Panda Cam\\nConnection\\nSuccessful\\n\\nMonitoring active\\n{current_time}",
            "bg_color": "lightgreen",
            "text_color": "darkgreen"
        },
        "maintenance": {
            "text": f"🐼 Panda Cam\\nMaintenance\\n\\nCheck back later\\n{current_time}",
            "bg_color": "lightgray",
            "text_color": "darkred"
        },
        "rate_limited": {
            "text": f"🐼 Panda Cam\\nRate Limited\\n\\nTrying again soon\\n{current_time}",
            "bg_color": "lightyellow",
            "text_color": "darkorange"
        }
    }
    
    config = status_configs.get(status_type, status_configs["unavailable"])
    
    # Using a simple text file instead of ImageMagick since it's not available locally
    demo_content = f"""
# Panda Cam Status Demo: {status_type.title()}

## Visual Representation
Background Color: {config['bg_color']}
Text Color: {config['text_color']}
Size: 800x600 pixels

## Status Text:
{config['text'].replace('\\n', ' | ')}

## Description:
{description}

## Technical Details:
- Generated: {time.strftime("%Y-%m-%d %H:%M:%S UTC")}
- Status Type: {status_type}
- Workflow: Enhanced Panda Cam Monitor
- Method: Dynamic ImageMagick generation in GitHub Actions

---
This would be a color-coded image in the actual workflow!
"""
    
    with open(f'demo_status_{status_type}.txt', 'w') as f:
        f.write(demo_content)
    
    print(f"✅ Created demo for {status_type} status")

def main():
    print("🎨 Creating Panda Cam Status Image Demonstrations")
    print("=" * 55)
    
    status_examples = {
        "unavailable": "When zoo webcam blocks automated access (HTTP 403)",
        "accessible": "When connection is successful and monitoring is active", 
        "maintenance": "When webcam is temporarily down or in maintenance",
        "rate_limited": "When too many requests have been made recently"
    }
    
    for status_type, description in status_examples.items():
        create_demo_image(status_type, description)
    
    print("\n🎯 Demo files created!")
    print("📁 Check the demo_status_*.txt files to see what the actual images would look like.")
    print("\n💡 In the GitHub Actions environment, these become actual PNG images with:")
    print("   - Color-coded backgrounds")
    print("   - Professional typography") 
    print("   - Emoji status indicators")
    print("   - Real-time timestamps")

if __name__ == "__main__":
    main()
