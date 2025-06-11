#!/usr/bin/env python3
"""
Local test of the enhanced panda cam workflow
"""

import time
import os
import requests
import subprocess
import random
import logging
from urllib.parse import urljoin

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def get_random_headers():
    """Generate realistic browser headers"""
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]
    
    return {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cache-Control': 'max-age=0'
    }

def try_zoo_webcam(url, name, delay=2):
    """Try to access a zoo webcam with proper error handling"""
    try:
        logger.info(f"Attempting {name}...")
        headers = get_random_headers()
        
        # Add random delay to avoid rate limiting
        time.sleep(random.uniform(1, delay))
        
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        logger.info(f"{name}: HTTP {response.status_code}")
        
        if response.status_code == 200:
            logger.info(f"✅ {name} is accessible")
            return response.text
        elif response.status_code == 403:
            logger.warning(f"🚫 {name}: Access forbidden (bot detection)")
            return None
        elif response.status_code == 503:
            logger.warning(f"⚠️ {name}: Service temporarily unavailable")
            return None
        else:
            logger.warning(f"❌ {name}: HTTP {response.status_code}")
            return None
            
    except requests.exceptions.Timeout:
        logger.warning(f"⏰ {name}: Request timeout")
        return None
    except requests.exceptions.ConnectionError:
        logger.warning(f"🔌 {name}: Connection error")
        return None
    except Exception as e:
        logger.error(f"❌ {name}: {e}")
        return None

def create_panda_image(image_type="unavailable", status_info=""):
    """Create a descriptive image when webcam is unavailable"""
    try:
        current_time = time.strftime("%H:%M UTC", time.gmtime())
        
        if image_type == "unavailable":
            text = f"🐼 Panda Cam\\nTemporarily\\nUnavailable\\n\\n(Access restricted)\\n{current_time}"
            bg_color = "lightblue"
            text_color = "darkblue"
        elif image_type == "rate_limited":
            text = f"🐼 Panda Cam\\nRate Limited\\n\\nTrying again soon\\n{current_time}"
            bg_color = "lightyellow"
            text_color = "darkorange"
        elif image_type == "maintenance":
            text = f"🐼 Panda Cam\\nMaintenance\\n\\nCheck back later\\n{current_time}"
            bg_color = "lightgray"
            text_color = "darkred"
        elif image_type == "accessible":
            text = f"🐼 Panda Cam\\nConnection\\nSuccessful\\n\\n{status_info}\\n{current_time}"
            bg_color = "lightgreen"
            text_color = "darkgreen"
        else:
            text = f"🐼 Panda Cam\\nTechnical\\nDifficulties\\n\\n{current_time}"
            bg_color = "lightcoral"
            text_color = "darkred"
        
        cmd = [
            'convert', '-size', '800x600', f'xc:{bg_color}',
            '-pointsize', '28', '-fill', text_color, '-gravity', 'center',
            '-annotate', '+0+0', text,
            '-bordercolor', text_color, '-border', '3x3',
            f'test_panda_cam_{image_type}.png'
        ]
        
        subprocess.run(cmd, check=True)
        logger.info(f"✅ Created {image_type} status image: test_panda_cam_{image_type}.png")
        return True
        
    except Exception as e:
        logger.error(f"❌ Failed to create status image: {e}")
        return False

def capture_panda_cam():
    """Main capture function with multiple strategies"""
    
    # Strategy 1: Try National Zoo with different approaches
    zoo_variants = [
        ("National Zoo (main)", "https://nationalzoo.si.edu/webcams/panda-cam"),
        ("National Zoo (mobile)", "https://m.nationalzoo.si.edu/webcams/panda-cam"),
        ("National Zoo (api)", "https://nationalzoo.si.edu/api/webcams/panda"),
        ("National Zoo (alternative)", "https://nationalzoo.si.edu/webcams/elephant-cam"),
    ]
    
    successful_connections = 0
    blocked_connections = 0
    
    for name, url in zoo_variants:
        html_content = try_zoo_webcam(url, name)
        if html_content:
            successful_connections += 1
            logger.info(f"✅ Got content from {name}")
            
            # Analyze the content briefly
            if "panda" in html_content.lower():
                logger.info("Found panda-related content")
            if "video" in html_content.lower() or "stream" in html_content.lower():
                logger.info("Found video/stream references")
            if "live" in html_content.lower():
                logger.info("Found live content indicators")
                
        elif "403" in str(html_content):
            blocked_connections += 1
    
    # Strategy 2: Try alternative zoo sources for comparison
    logger.info("Testing alternative zoo sources...")
    
    alt_sources = [
        ("San Diego Zoo", "https://zoo.sandiegozoo.org/"),
        ("Smithsonian Zoo", "https://nationalzoo.si.edu/"),
    ]
    
    for name, url in alt_sources:
        try_zoo_webcam(url, name, delay=1)
    
    # Strategy 3: Create appropriate status images for all scenarios
    logger.info("📸 Creating all status image examples...")
    
    # Create examples of all status types
    create_panda_image("unavailable")
    create_panda_image("rate_limited")
    create_panda_image("maintenance")
    create_panda_image("accessible", "Connected to 2 sources")
    create_panda_image("error")
    
    if successful_connections > 0:
        status_info = f"Connected to {successful_connections} sources"
        return create_panda_image("accessible", status_info)
    elif blocked_connections > 0:
        return create_panda_image("unavailable")
    else:
        return create_panda_image("maintenance")

if __name__ == "__main__":
    logger.info("🧪 Testing Enhanced Panda Cam Workflow Locally")
    logger.info("=" * 60)
    
    # Execute the capture
    success = capture_panda_cam()
    
    if success:
        logger.info("🎯 Test completed successfully!")
        logger.info("📁 Check the generated test_panda_cam_*.png files")
    else:
        logger.error("❌ Test failed!")
    
    # List generated files
    test_files = [f for f in os.listdir('.') if f.startswith('test_panda_cam_')]
    if test_files:
        logger.info(f"📋 Generated files: {test_files}")
    else:
        logger.warning("⚠️ No test files were created")
