# obs-wayland

OBS Studio integration tool for Wayland compositors. Control OBS Studio from outside the application when global shortcuts are broken (e.g., KDE Plasma + Wayland).

## Problem

KDE Plasma with Wayland can break OBS Studio's global shortcuts, making it impossible to control recording, streaming, virtual camera, scene switching, and source toggling from outside the application.

## Solution

`obs-wayland` provides a command-line tool that runs outside OBS and communicates via the OBS WebSocket API. You can:

- Start/stop recording
- Start/stop streaming
- Start/stop virtual camera
- Switch between scenes
- Toggle audio sources (mute/unmute)
- Integrate with custom key bindings, scripts, or automation tools

## Requirements

- Python 3.12+
- OBS Studio with WebSocket server enabled
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Installation

### Using uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/dxas90/obs-wayland.git
cd obs-wayland

# Install as a user tool
uv tool install --editable .
```

### Using pip

```bash
pip install --user -e .
```

## Configuration

### 1. Enable OBS WebSocket Server

In OBS Studio:

1. Go to **Tools → WebSocket Server Settings**
2. Enable the WebSocket server
3. Note the port (default: 4455)
4. Copy the password shown

### 2. Create Configuration File

Create a configuration directory and file:

```bash
mkdir -p ~/.config/obs-wayland
```

Create `~/.config/obs-wayland/.env` with the following content:

```bash
# OBS WebSocket Configuration
OBS_HOST=localhost
OBS_PORT=4455
OBS_PASSWORD=your-obs-websocket-password-here
```

Replace `your-obs-websocket-password-here` with the actual password from OBS WebSocket Server Settings.

### Configuration File Locations

The tool looks for `.env` files in this order:

1. `~/.config/obs-wayland/.env` (recommended for system-wide installation)
2. `./.env` (current working directory)
3. Environment variables

## Usage

### Basic Commands

```bash
# Toggle recording (start/stop)
obs-keys record

# Toggle streaming (start/stop)
obs-keys stream

# Toggle virtual camera (start/stop)
obs-keys virtualcam

# Switch to a specific scene
obs-keys scene "Scene Name"

# Toggle an audio source (mute/unmute)
obs-keys input_toggle "Mic/Aux"
```

### Examples

```bash
# Start/stop recording
obs-keys record

# Start/stop streaming
obs-keys stream

# Start/stop virtual camera
obs-keys virtualcam

# Switch to your desktop scene
obs-keys scene "Desktop"

# Switch to your camera scene
obs-keys scene "Camera"

# Mute/unmute microphone
obs-keys input_toggle "Mic/Aux"

# Toggle desktop audio
obs-keys input_toggle "Desktop Audio"
```

### Integration with Custom Key Bindings

You can bind these commands to custom keyboard shortcuts in your desktop environment or window manager.

#### KDE Plasma

1. Go to **System Settings → Shortcuts → Custom Shortcuts**
2. Create a new shortcut
3. Set the command to: `obs-keys record` (or any other command)
4. Assign your desired key combination

Example shortcuts:

- `Meta+F9` → `obs-keys record`
- `Meta+F10` → `obs-keys stream`
- `Meta+F11` → `obs-keys virtualcam`
- `Meta+F12` → `obs-keys input_toggle "Mic/Aux"`

#### i3/sway

Add to your `~/.config/i3/config` or `~/.config/sway/config`:

```conf
bindsym $mod+F9 exec obs-keys record
bindsym $mod+F10 exec obs-keys stream
bindsym $mod+F11 exec obs-keys virtualcam
bindsym $mod+F12 exec obs-keys input_toggle "Mic/Aux"
```

#### GNOME

Use the GNOME Settings or install `gnome-tweaks`:

```bash
gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings \
  "['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/']"

gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ \
  name 'OBS Record'

gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ \
  command 'obs-keys record'

gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ \
  binding '<Super>F9'
```

### Using with Scripts

```bash
#!/bin/bash
# Start recording, wait 10 seconds, stop recording

obs-keys record
sleep 10
obs-keys record
```

## Development

### Project Structure

```text
obs-wayland/
├── obs_wayland/          # Main package
│   ├── __init__.py       # Package initialization
│   └── __main__.py       # Main entry point with CLI logic
├── pyproject.toml        # Project configuration
├── mise.toml             # Development environment (optional)
├── .env.example          # Example configuration
└── README.md             # This file
```

### Local Development

```bash
# Clone and enter directory
git clone https://github.com/dxas90/obs-wayland.git
cd obs-wayland

# Install in editable mode
uv tool install --editable .

# Run directly from source
uv run python -m obs_wayland record

# Or with the installed command
obs-keys record
```

### Dependencies

- **obsws-python**: OBS WebSocket Python library
- **python-dotenv**: Environment variable management

## Troubleshooting

### "authentication enabled but no password provided"

- Ensure your `.env` file exists at `~/.config/obs-wayland/.env`
- Verify the `OBS_PASSWORD` is set correctly
- Check that OBS WebSocket server is enabled and the password matches

### "No module named 'obs_wayland'"

- Reinstall the package: `uv tool install --force --editable .`
- Ensure the installation completed successfully

### Connection refused

- Verify OBS Studio is running
- Check that WebSocket server is enabled in OBS (Tools → WebSocket Server Settings)
- Ensure the port in `.env` matches the OBS WebSocket port (default: 4455)
- Try connecting to `localhost` first before using remote connections

### Scene or Input Not Found

- Ensure the scene name or input name exactly matches what's in OBS
- Scene and input names are case-sensitive
- Use quotes if the name contains spaces: `obs-keys scene "My Scene"`

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Daniel Ramirez <dxas90@gmail.com>
