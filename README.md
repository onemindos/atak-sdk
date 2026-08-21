# atak-sdk

OneMind ATAK shared SDK — Python package providing NATS client, CoT utilities, TAK API helpers, and HUD theming for OneMind ATAK plugins and services.

---

## Install

```bash
pip install -e .
# or from GitHub:
pip install git+https://github.com/onemindos/atak-sdk.git
```

**Requirements:** Python 3.10+, `nats-py>=2.6.0`, `requests>=2.31.0`

---

## Modules

| Module | Description |
|--------|-------------|
| `onemind_atak.nats_client` | Async NATS client wrapper — connect, publish, subscribe with reconnect |
| `onemind_atak.cot_utils` | CoT XML builder/parser — position, 9-line, sensor point, chat |
| `onemind_atak.tak_api` | REST helpers for TAK Server API (Marti endpoints) |
| `onemind_atak.hud_theme` | Shared color constants and draw primitives for Kivy HUD plugins |

---

## Quick start

```python
import asyncio
from onemind_atak import nats_client, cot_utils

async def main():
    nc = await nats_client.connect("nats://localhost:4222")

    # Publish a CoT position
    cot = cot_utils.position(
        uid="ANDROID-zeus-01",
        callsign="Zeus",
        lat=37.7749,
        lon=-122.4194,
        alt=363,
        course=310,
        speed=0,
    )
    await nc.publish("onemind.cot", cot.encode())
    await nc.close()

asyncio.run(main())
```

---

## Used by

- [`atak-plugin-omhud`](https://github.com/onemindos/atak-plugin-omhud) — tactical AR HUD overlay

---

## License

Apache 2.0 — OneMind OS
