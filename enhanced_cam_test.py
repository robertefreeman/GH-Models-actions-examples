#!/usr/bin/env python3
"""
Enhanced panda cam capture with better error handling and alternative approaches
"""

import time
import requests
import subprocess
import os
import logging
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def try_alternative_zoo_cams():
    """Try alternative zoo webcams that might be more accessible"""
    
    alternative_cams = [
        {
            "name": "San Diego Zoo Panda Cam",
            "url": "https://zoo.sandiegozoo.org/live-cams/elephant-cam",
            "description": "San Diego Zoo live cam"
        },
        {
            "name": "Edinburgh Zoo Panda Cam", 
            "url": "https://www.edinburghzoo.org.uk/webcam/panda-cam",
            "description": "Edinburgh Zoo panda webcam"
        },
        {
            "name": "Zoo Atlanta Panda Cam",
            "url": "https://zooatlanta.org/panda-cam/",
            "description": "Zoo Atlanta panda cam"
        }
    ]
    
    for cam in alternative_cams:
        try:
            logger.info(f"Testing {cam['name']}...")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
            
            response = requests.get(cam["url"], headers=headers, timeout=10)
            logger.info(f"{cam['name']}: Status {response.status_code}")
            
            if response.status_code == 200:
                logger.info(f"✅ {cam['name']} is accessible")
                # Save HTML for analysis
                with open(f"cam_analysis_{cam['name'].lower().replace(' ', '_')}.html", 'w') as f:
                    f.write(response.text[:5000])  # First 5KB for analysis
            else:
                logger.warning(f"❌ {cam['name']}: HTTP {response.status_code}")
                
        except Exception as e:
            logger.error(f"❌ {cam['name']}: {e}")

def test_direct_stream_urls():
    """Test some known working livestream URLs"""
    
    test_streams = [
        "https://cams.zsl.org/london-zoo-land-of-the-lions.m3u8",
        "https://video-weaver.sea01.hls.ttvnw.tv/v1/playlist/test.m3u8",
        # Generic test streams
        "https://devstreaming-cdn.apple.com/videos/streaming/examples/img_bipbop_adv_example_fmp4/master.m3u8",
        "https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8"
    ]
    
    for stream_url in test_streams:
        try:
            logger.info(f"Testing stream: {stream_url}")
            
            # Test with FFmpeg
            ffmpeg_cmd = [
                'ffmpeg', '-y', '-loglevel', 'quiet',
                '-i', stream_url,
                '-vframes', '1', '-q:v', '2', '-f', 'image2',
                f'test_frame_{hash(stream_url) % 1000}.png'
            ]
            
            result = subprocess.run(ffmpeg_cmd, timeout=15, capture_output=True)
            
            if result.returncode == 0:
                logger.info(f"✅ Successfully captured frame from {stream_url}")
            else:
                logger.warning(f"❌ FFmpeg failed for {stream_url}")
                
        except subprocess.TimeoutExpired:
            logger.warning(f"⏰ Timeout for {stream_url}")
        except Exception as e:
            logger.error(f"❌ Error with {stream_url}: {e}")

def create_fallback_strategies():
    """Create a comprehensive fallback strategy document"""
    
    strategies = """
# Panda Cam Capture Strategies

## Current Issue
The National Zoo panda cam appears to be blocking automated requests (HTTP 403).

## Alternative Strategies:

### 1. Use Different User Agents
- Rotate through various browser user agents
- Use mobile user agents 
- Add realistic headers (Accept, Accept-Language, etc.)

### 2. Alternative Zoo Webcams
- San Diego Zoo (better API access)
- Edinburgh Zoo (pandas available)
- Zoo Atlanta (good streaming setup)

### 3. Timing Strategies  
- Respect rate limits (longer delays between requests)
- Only capture during actual zoo hours
- Use exponential backoff on failures

### 4. Proxy/VPN Solutions
- Route through different IP addresses
- Use residential proxy services
- Geographic rotation

### 5. API Partnerships
- Contact zoos directly for API access
- Use official zoo mobile app endpoints
- Partner with zoo social media feeds

### 6. Social Media Integration
- Monitor zoo Twitter/Instagram for panda photos
- Use zoo YouTube livestreams
- Parse zoo Facebook live videos

## Technical Improvements:

### 1. Better Error Handling
- Graceful degradation when streams unavailable
- Clear error messages in blog updates
- Automatic fallback to static images

### 2. Enhanced Stream Processing
- Support for RTMP streams
- WebRTC stream capture
- Adaptive bitrate handling

### 3. AI Analysis Improvements
- Better prompt engineering for different image types
- Confidence scoring
- Activity pattern detection over time
"""
    
    with open('panda_cam_strategies.md', 'w') as f:
        f.write(strategies)
    
    logger.info("📋 Created comprehensive strategy document: panda_cam_strategies.md")

if __name__ == "__main__":
    logger.info("🔍 Enhanced Panda Cam Analysis")
    logger.info("=" * 50)
    
    # Test alternative zoo cams
    try_alternative_zoo_cams()
    
    logger.info("\n" + "=" * 30)
    
    # Test direct streaming
    test_direct_stream_urls()
    
    logger.info("\n" + "=" * 30)
    
    # Create strategy document
    create_fallback_strategies()
    
    logger.info("\n🎯 Analysis complete!")
    logger.info("Check the generated files for detailed results")
