# blucli Skill

Bluetooth device management via blucli CLI on macOS.

## Use When
- Connecting/disconnecting Bluetooth devices
- Listing paired Bluetooth devices
- Checking Bluetooth device status

## Commands
```bash
# List all paired devices
blucli list

# Connect to device
blucli connect "AirPods Pro"

# Disconnect from device
blucli disconnect "AirPods Pro"

# Check device status
blucli status "AirPods Pro"

# Toggle Bluetooth on/off
blucli power on
blucli power off
```

## Install
```bash
brew install nickcoutsos/tap/blucli
```

## Notes
- macOS only
- Device names are case-sensitive
- Run with sudo if permission errors occur
- Bluetooth must be enabled in System Settings
