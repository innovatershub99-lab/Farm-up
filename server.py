#!/usr/bin/env python3
"""
Simple HTTP server for FarmUp application
Run this to serve the static files locally for testing
"""

import http.server
import socketserver
import os
import webbrowser
from threading import Timer

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="public", **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def open_browser():
    webbrowser.open('http://localhost:8000')

if __name__ == "__main__":
    PORT = 8000
    
    # Change to the farmup directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🌱 FarmUp Development Server")
        print(f"📍 Serving at http://localhost:{PORT}")
        print(f"📁 Serving files from: {os.path.join(os.getcwd(), 'public')}")
        print(f"🚀 Opening browser in 2 seconds...")
        print(f"💡 Press Ctrl+C to stop the server")
        
        # Open browser after 2 seconds
        Timer(2.0, open_browser).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n🛑 Server stopped")
            httpd.shutdown()