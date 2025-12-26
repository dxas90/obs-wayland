#!/usr/bin/env python

import sys
import os
from pathlib import Path
import obsws_python as obs
from dotenv import load_dotenv

# Look for .env file in multiple locations (in order of preference)
config_dir = Path.home() / ".config" / "obs-wayland"
cwd_env = Path.cwd() / ".env"
config_env = config_dir / ".env"

if config_env.exists():
    load_dotenv(config_env)
elif cwd_env.exists():
    load_dotenv(cwd_env)
else:
    # Try to load from environment variables only
    load_dotenv()

# Get OBS WebSocket credentials from environment
obs_host = os.getenv("OBS_HOST", "localhost")
obs_port = int(os.getenv("OBS_PORT", "4455"))
obs_password = os.getenv("OBS_PASSWORD", "")

# Initialize OBS WebSocket client
cl = obs.ReqClient(host=obs_host, port=obs_port, password=obs_password)

def toggle_record():
    r = cl.get_record_status()
    if r.output_active:
        cl.stop_record()
    else:
        cl.start_record()

def toggle_stream():
    s = cl.get_stream_status()
    if s.output_active:
        cl.stop_stream()
    else:
        cl.start_stream()

def toggle_virtual_camera():
    vc = cl.get_virtual_cam_status()
    if vc.output_active:
        cl.stop_virtual_cam()
    else:
        cl.start_virtual_cam()

def switch_scene(scene_name):
    cl.set_current_program_scene(scene_name)

def toggle_input(input_name):
    state = cl.get_input_mute(input_name).input_muted
    cl.set_input_mute(input_name, not state)

def print_help():
    print("""
Usage:
  obs-keys record                    # Toggle recording
  obs-keys stream                    # Toggle streaming
  obs-keys virtualcam                # Toggle virtual camera
  obs-keys scene <scene_name>        # Switch to scene
  obs-keys input_toggle <input_name> # Toggle audio source mute
""")

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    action = sys.argv[1]

    if action == "record":
        toggle_record()

    elif action == "stream":
        toggle_stream()

    elif action == "virtualcam":
        toggle_virtual_camera()

    elif action == "scene" and len(sys.argv) >= 3:
        switch_scene(sys.argv[2])

    elif action == "input_toggle" and len(sys.argv) >= 3:
        toggle_input(sys.argv[2])

    else:
        print_help()

if __name__ == "__main__":
    main()
