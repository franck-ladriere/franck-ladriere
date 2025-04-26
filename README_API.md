# SmartHomePilot API Documentation

## Endpoints

- `POST /devices/on` : Turn a device ON
- `POST /devices/off` : Turn a device OFF
- `GET /status` : Retrieve the status of all devices

## Example Request

```bash
curl -X POST https://api.smarthomepilot.com/devices/on -d '{"device": "Living Room Light"}'
