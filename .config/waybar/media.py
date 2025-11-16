#!/usr/bin/env python3
import subprocess
import json
import sys

def get_player_status():
    """Get current media player status using playerctl"""
    try:
        # Try to get Spotify first, then any player
        player_args = []
        
        # Check if spotify is available
        players = subprocess.check_output(
            ['playerctl', '-l'], 
            stderr=subprocess.DEVNULL
        ).decode('utf-8').strip().split('\n')
        
        if 'spotify' in players:
            player_args = ['-p', 'spotify']
        
        # Get player status
        status = subprocess.check_output(
            ['playerctl'] + player_args + ['status'], 
            stderr=subprocess.DEVNULL
        ).decode('utf-8').strip()
        
        # Get metadata
        artist = subprocess.check_output(
            ['playerctl'] + player_args + ['metadata', 'artist'], 
            stderr=subprocess.DEVNULL
        ).decode('utf-8').strip()
        
        title = subprocess.check_output(
            ['playerctl'] + player_args + ['metadata', 'title'], 
            stderr=subprocess.DEVNULL
        ).decode('utf-8').strip()
        
        # Create display text
        if status == "Playing":
            icon = "󰏤"  # Play icon
            text = f"{artist} - {title}"
        elif status == "Paused":
            icon = "󰐊"  # Pause icon
            text = f"{artist} - {title}"
        else:
            icon = ""  # Stop icon
            text = ""
        
        # Truncate long text
        max_length = 50
        if len(text) > max_length:
            text = text[:max_length-3] + "..."
        
        output = {
            "text": f"{icon} {text}",
            "tooltip": f"{artist}\n{title}\nStatus: {status}",
            "class": status.lower(),
            "alt": status
        }
        
        print(json.dumps(output))
        
    except subprocess.CalledProcessError:
        # No player running
        output = {
            "text": "",
            "tooltip": "No media player running",
            "class": "stopped"
        }
        print(json.dumps(output))
    except Exception as e:
        output = {
            "text": "󰝚 Error",
            "tooltip": str(e),
            "class": "error"
        }
        print(json.dumps(output))

def toggle_play_pause():
    """Toggle play/pause"""
    try:
        # Check if spotify is available
        players = subprocess.check_output(
            ['playerctl', '-l'], 
            stderr=subprocess.DEVNULL
        ).decode('utf-8').strip().split('\n')
        
        if 'spotify' in players:
            subprocess.run(['playerctl', '-p', 'spotify', 'play-pause'], check=True)
        else:
            subprocess.run(['playerctl', 'play-pause'], check=True)
    except:
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "toggle":
        toggle_play_pause()
    else:
        get_player_status()
