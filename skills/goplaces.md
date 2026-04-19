# GoPlaces Skill

Location and places lookup — find nearby places, get directions, geocode addresses.

## Use When
- Finding restaurants, shops, or services near a location
- Geocoding addresses to coordinates
- Getting directions or travel times

## Google Maps API
```bash
export GOOGLE_MAPS_KEY="your-key"

# Nearby places search
curl "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=51.5,-0.1&radius=500&type=restaurant&key=$GOOGLE_MAPS_KEY" | jq '.results[:3] | .[] | {name, vicinity, rating}'

# Geocode address
curl "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Pkwy,+Mountain+View,+CA&key=$GOOGLE_MAPS_KEY" | jq '.results[0].geometry.location'

# Directions
curl "https://maps.googleapis.com/maps/api/directions/json?origin=London&destination=Paris&mode=driving&key=$GOOGLE_MAPS_KEY" | jq '.routes[0].legs[0] | {distance:.distance.text, duration:.duration.text}'
```

## Free Alternatives (no key needed)
```bash
# Nominatim geocoding (OpenStreetMap)
curl "https://nominatim.openstreetmap.org/search?q=Empire+State+Building&format=json&limit=1" | jq '.[0] | {lat, lon, display_name}'

# Reverse geocode
curl "https://nominatim.openstreetmap.org/reverse?lat=40.748&lon=-73.985&format=json" | jq '.display_name'
```

## Notes
- Google Maps API requires billing enabled (generous free tier)
- Nominatim is free, add User-Agent header for politeness
- Rate limit Nominatim: max 1 request/second
