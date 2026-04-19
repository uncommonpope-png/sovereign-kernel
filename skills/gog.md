# GOG Skill

Manage GOG Galaxy game library and downloads via GOG CLI or API.

## Use When
- Listing GOG game library
- Downloading or installing GOG games
- Managing GOG Galaxy client

## lgogdownloader CLI (recommended)
```bash
# Login
lgogdownloader --login

# List library
lgogdownloader --list

# Download game
lgogdownloader --download --game "witcher_3"

# Download specific platform/language
lgogdownloader --download --game "witcher_3" --platform 4 --language 1

# Update all games
lgogdownloader --download --update-only
```

## GOG Galaxy API (unofficial)
```bash
# Auth via GOG login page — capture token from browser
TOKEN="your-token"

# Get library
curl -H "Authorization: Bearer $TOKEN" \
  "https://menu.gog.com/v1/account/licences"

# Get game details
curl "https://api.gog.com/products/<game-id>?expand=downloads"
```

## Platforms
- 1 = Windows, 2 = macOS, 4 = Linux

## Notes
- lgogdownloader is the primary open-source CLI for GOG
- DRM-free downloads — games are yours to keep
- brew install lgogdownloader (Linux/macOS)
