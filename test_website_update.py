#!/usr/bin/env python3
"""
Test the website update functionality locally
"""

import re
import os
from datetime import datetime

def test_website_update():
    """Test our website update logic with the current panda analysis"""
    
    print("🧪 Testing Website Update Logic")
    print("=" * 50)
    
    # Use the actual current panda analysis
    try:
        with open('webpage/actionsblog.md', 'r') as f:
            blog_content = f.read()
        
        # Extract the latest analysis from the blog
        analysis_match = re.search(r'## 🐼 Live Panda Cam Analysis.*?(?=##|\Z)', blog_content, re.DOTALL)
        if analysis_match:
            analysis = analysis_match.group(0)
            print("📄 Found panda analysis in blog:")
            print("  " + "\n  ".join(analysis.split('\n')[:5]))  # First 5 lines
        else:
            analysis = "Monitoring system active"
            print("📄 No panda analysis found, using default")
            
    except FileNotFoundError:
        analysis = "Monitoring system active"
        print("📄 Blog file not found, using default analysis")
    
    # Generate status summary
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    print(f"\n🔍 Analysis keywords found:")
    present_words = [word for word in ['present', 'visible', 'panda', 'eating', 'active', 'chewing', 'bamboo'] if word in analysis.lower()]
    unavail_words = [word for word in ['unavailable', 'restricted', 'blocked', 'forbidden'] if word in analysis.lower()]
    maint_words = [word for word in ['maintenance', 'down', 'error'] if word in analysis.lower()]
    
    print(f"  Present indicators: {present_words}")
    print(f"  Unavailable indicators: {unavail_words}")
    print(f"  Maintenance indicators: {maint_words}")
    
    if present_words:
        status_summary = f"🐼 Panda spotted! - Last updated: {timestamp}"
        status_color = "#4caf50"
        status_type = "PANDA VISIBLE"
    elif unavail_words:
        status_summary = f"📡 Webcam temporarily unavailable - Last updated: {timestamp}"  
        status_color = "#ff9800"
        status_type = "UNAVAILABLE"
    elif maint_words:
        status_summary = f"🔧 Webcam under maintenance - Last updated: {timestamp}"
        status_color = "#f44336"
        status_type = "MAINTENANCE"
    else:
        status_summary = f"🔄 Currently monitoring - Last updated: {timestamp}"
        status_color = "#2196f3"
        status_type = "MONITORING"
    
    print(f"\n🎯 Generated Status:")
    print(f"  Type: {status_type}")
    print(f"  Summary: {status_summary}")
    print(f"  Color: {status_color}")
    
    # Show what the HTML section would look like
    html_section = f'''
<div class="highlight-box" style="margin-top: 15px; background: linear-gradient(135deg, #e3f2fd 0%, #f1f8e9 100%); border-left: 4px solid {status_color};">
    <h4><span class="emoji">🐼</span> Live Panda Cam Status</h4>
    <p><strong>{status_summary}</strong></p>
    <div style="font-size: 0.9em; color: #666; margin-top: 10px;">
        <em>This status is automatically updated every 30 minutes during zoo hours using AI vision analysis.</em>
    </div>
    <div style="margin-top: 10px;">
        <a href="https://github.com/robertefreeman/GH-Models-actions-examples/blob/main/webpage/actionsblog.md#-live-panda-cam-analysis" 
           style="color: #1976d2; text-decoration: none; font-weight: bold;">→ View detailed analysis</a>
    </div>
</div>'''
    
    print(f"\n🌐 HTML Section Preview:")
    print("=" * 50)
    print(html_section)
    print("=" * 50)
    
    print(f"\n✅ Website update test completed!")
    print(f"📊 This would be injected into index.html after the Panda Cam AI Monitor section")

if __name__ == "__main__":
    test_website_update()
