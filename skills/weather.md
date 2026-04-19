# Weather Skill

Easily access current weather conditions and forecasts using wttr.in (no API key required).

## Use When
- The user inquires about weather, temperature, rain, or forecasts for a specific location.
- The user needs to check weather conditions for travel or outdoor activities.

## Features
- Retrieve current weather details (temperature, conditions, wind).
- Access a 3-day or detailed weather forecast.
- Flexible location input (city or airport codes supported).
- Plain text or JSON output options for custom use cases.

## Usage

### Current Weather  
Quickly fetch the current weather for a given location:  
```bash
curl "wttr.in/[LOCATION]?format=3"
# Example:
curl "wttr.in/London?format=3"
```

### Customized Format  
Request weather with a tailored output format, including city name, condition, temperature, and wind:  
```bash
curl "wttr.in/[LOCATION]?format=%l:+%c+%t+%w"
# Example:
curl "wttr.in/New+York?format=%l:+%c+%t+%w"
```

### 3-Day Forecast  
Retrieve a 3-day weather forecast in a simple text format:  
```bash
curl "wttr.in/[LOCATION]"
# Example:
curl "wttr.in/Paris"
```

### JSON Output  
Fetch weather data in JSON format for integration into other tools or applications:  
```bash
curl "wttr.in/[LOCATION]?format=j1"
# Example:
curl "wttr.in/Tokyo?format=j1"
```

## Notes  
- Replace `[LOCATION]` with the desired city name or location code (e.g., `London`, `LAX`).
- Inputs are not case-sensitive.
- Ensure proper URL encoding for multi-word locations (e.g., `New+York`).

## Example Commands  
- Current weather summary for San Francisco:  
  ```bash
  curl "wttr.in/San+Francisco?format=3"
  ```
- 3-day weather forecast for Tokyo:  
  ```bash
  curl "wttr.in/Tokyo"
  ``` 

This compact utility is an efficient tool for quick and detailed weather information anywhere in the world.