#!/usr/bin/env python3
"""
Test script to simulate the enhanced HLS video capture locally
This tests our video stream detection and capture logic
"""

import requests
import re
import subprocess
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_page_analysis():
    """Test our page analysis for video streams"""
    try:
        logger.info("Fetching panda cam page...")
        response = requests.get("https://nationalzoo.si.edu/webcams/panda-cam", 
                              headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        
        if response.status_code == 200:
            html_content = response.text
            
            # Look for various video URL patterns
            patterns = [
                r'https?://[^\s"\']+\.m3u8[^\s"\']*',  # HLS streams
                r'https?://[^\s"\']+\.mp4[^\s"\']*',   # MP4 videos
                r'https?://[^\s"\']+/live[^\s"\']*',   # Live streams
                r'https?://[^\s"\']+stream[^\s"\']*',  # Stream URLs
                r'src="([^"]*(?:youtube|vimeo|livestream)[^"]*)"',  # Embedded videos
                r'blob:[^\s"\']+',  # Blob URLs
                r'hls-container[^>]*src="([^"]*)"',  # HLS container elements
            ]
            
            found_urls = []
            for pattern in patterns:
                matches = re.findall(pattern, html_content, re.IGNORECASE)
                if matches:
                    logger.info(f"Pattern '{pattern}' found: {matches}")
                    found_urls.extend(matches)
            
            # Look for video elements in the HTML
            video_pattern = r'<video[^>]*>'
            video_matches = re.findall(video_pattern, html_content, re.IGNORECASE)
            if video_matches:
                logger.info(f"Found video elements: {video_matches}")
            
            # Look for HLS.js or video.js references
            hls_js_pattern = r'hls\.js|video\.js|jwplayer'
            if re.search(hls_js_pattern, html_content, re.IGNORECASE):
                logger.info("Found HLS.js or video player references")
            
            # Check for common streaming platforms
            streaming_patterns = [
                r'youtube\.com/embed/([a-zA-Z0-9_-]+)',
                r'vimeo\.com/video/(\d+)',
                r'twitch\.tv/embed/([a-zA-Z0-9_]+)',
            ]
            
            for pattern in streaming_patterns:
                matches = re.findall(pattern, html_content)
                if matches:
                    logger.info(f"Found streaming platform content: {matches}")
            
            # Save a snippet of the HTML for analysis
            with open('panda_page_snippet.html', 'w') as f:
                # Find the video-related section
                lines = html_content.split('\n')
                video_lines = []
                for i, line in enumerate(lines):
                    if any(keyword in line.lower() for keyword in ['video', 'stream', 'cam', 'live']):
                        # Include context around video-related lines
                        start = max(0, i-3)
                        end = min(len(lines), i+4)
                        video_lines.extend(lines[start:end])
                        video_lines.append('---')
                
                f.write('\n'.join(video_lines))
            
            logger.info("Analysis complete. Check panda_page_snippet.html for video-related HTML")
            
        else:
            logger.error(f"Failed to fetch page: {response.status_code}")
            
    except Exception as e:
        logger.error(f"Page analysis failed: {e}")

def test_ffmpeg_availability():
    """Test if FFmpeg is available and working"""
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            logger.info("FFmpeg is available")
            logger.info(f"FFmpeg version: {result.stdout.split('ffmpeg version')[1].split()[0]}")
            return True
        else:
            logger.error("FFmpeg is not working properly")
            return False
    except FileNotFoundError:
        logger.error("FFmpeg is not installed")
        return False
    except Exception as e:
        logger.error(f"FFmpeg test failed: {e}")
        return False

def test_yt_dlp_availability():
    """Test if yt-dlp is available"""
    try:
        result = subprocess.run(['yt-dlp', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            logger.info(f"yt-dlp is available: {result.stdout.strip()}")
            return True
        else:
            logger.error("yt-dlp is not working properly")
            return False
    except FileNotFoundError:
        logger.error("yt-dlp is not installed")
        return False
    except Exception as e:
        logger.error(f"yt-dlp test failed: {e}")
        return False

if __name__ == "__main__":
    logger.info("🐼 Testing Enhanced Panda Cam Capture")
    logger.info("=" * 50)
    
    # Test page analysis
    test_page_analysis()
    
    logger.info("\n" + "=" * 50)
    
    # Test tool availability
    ffmpeg_ok = test_ffmpeg_availability()
    yt_dlp_ok = test_yt_dlp_availability()
    
    logger.info(f"\nTool availability:")
    logger.info(f"  FFmpeg: {'✅' if ffmpeg_ok else '❌'}")
    logger.info(f"  yt-dlp: {'✅' if yt_dlp_ok else '❌'}")
    
    if os.path.exists('panda_page_snippet.html'):
        logger.info(f"\n📁 Created panda_page_snippet.html for analysis")
        logger.info("You can inspect this file to see the video-related HTML elements")
