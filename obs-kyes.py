import sys
import obsws_python as obs

cl = obs.ReqClient()

def toggle_record():
    r = cl.get_record_status()
    if r.output_active:
        cl.stop_record()
    else:
        cl.start_record()

def switch_scene(scene_name):
    cl.set_current_program_scene(scene_name)

def toggle_input(input_name):
    state = cl.get_input_mute(input_name).input_muted
    cl.set_input_mute(input_name, not state)

def print_help():
    print("""
Usage:
  obs_control.py record
  obs_control.py scene <scene_name>
  obs_control.py input_toggle <input_name>
""")

if len(sys.argv) < 2:
    print_help()
    sys.exit(1)

action = sys.argv[1]

if action == "record":
    toggle_record()

elif action == "scene" and len(sys.argv) >= 3:
    switch_scene(sys.argv[2])

elif action == "input_toggle" and len(sys.argv) >= 3:
    toggle_input(sys.argv[2])

else:
    print_help()
