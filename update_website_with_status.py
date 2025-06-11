#!/usr/bin/env python3
"""
Update the index.html file with live panda status
This simulates what the GitHub Actions workflow does
"""

import re
import os
from datetime import datetime

def update_website_with_status():
    """Update index.html with live panda status from the blog"""
    
    print("🌐 Updating Website with Live Panda Status")
    print("=" * 50)
    
    # Read the current panda analysis from the blog
    try:
        with open('webpage/actionsblog.md', 'r') as f:
            blog_content = f.read()
        
        # Extract the latest analysis from the blog
        analysis_match = re.search(r'## 🐼 Live Panda Cam Analysis.*?(?=##|\Z)', blog_content, re.DOTALL)
        if analysis_match:
            analysis = analysis_match.group(0)
            print("📄 Found panda analysis in blog")
        else:
            analysis = "Monitoring system active"
            print("📄 No panda analysis found, using default")
            
    except FileNotFoundError:
        analysis = "Monitoring system active"
        print("📄 Blog file not found, using default analysis")
    
    # Generate status summary
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    # Check for different status indicators
    present_words = [word for word in ['present', 'visible', 'panda', 'eating', 'active', 'chewing', 'bamboo'] if word in analysis.lower()]
    unavail_words = [word for word in ['unavailable', 'restricted', 'blocked', 'forbidden'] if word in analysis.lower()]
    maint_words = [word for word in ['maintenance', 'down', 'error'] if word in analysis.lower()]
    
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
    
    print(f"🎯 Status: {status_type} - {status_summary}")
    
    # Create the HTML section to inject
    live_status_html = f'''            <!-- LIVE PANDA STATUS - AUTO-GENERATED -->
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
            </div>
            <!-- END LIVE PANDA STATUS -->'''
    
    # Read the current index.html
    try:
        with open('index.html', 'r') as f:
            html_content = f.read()
    except FileNotFoundError:
        print("❌ index.html not found!")
        return
    
    # Remove any existing live status section
    html_content = re.sub(
        r'\s*<!-- LIVE PANDA STATUS - AUTO-GENERATED -->.*?<!-- END LIVE PANDA STATUS -->', 
        '', 
        html_content, 
        flags=re.DOTALL
    )
    
    # Find the Panda Cam section and inject the status after it
    panda_section_pattern = r'(<div class="use-case">\s*<strong>Use case:</strong> Showcasing computer vision integration and automated content generation with real-world data\.\s*</div>)'
    
    if re.search(panda_section_pattern, html_content):
        # Inject the live status after the use case div
        html_content = re.sub(
            panda_section_pattern,
            r'\1\n' + live_status_html,
            html_content
        )
        print("✅ Successfully injected live panda status into index.html")
        
        # Write the updated content back
        with open('index.html', 'w') as f:
            f.write(html_content)
        
        print("💾 Saved updated index.html")
        
    else:
        print("❌ Could not find Panda Cam section in index.html")
        print("Looking for pattern:", panda_section_pattern)
        return
    
    print("\n🎉 Website update completed!")
    print(f"📊 Live status now shows: {status_type}")

if __name__ == "__main__":
    update_website_with_status()
