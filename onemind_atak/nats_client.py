"""
OneMind NATS client — shared across all ATAK plugins.
Connects to the fabric with TLS, subscribes to subjects.
"""
import asyncio
import ssl
import os

try:
    import nats
except ImportError:
    nats = None


NATS_URL = os.environ.get("NATS_URL", "nats://nats.nats.svc.cluster.local:4222")
NATS_USER = os.environ.get("NATS_USER", "onemind")
NATS_PASS = os.environ.get("NATS_PASS", "")


async def connect(url=NATS_URL, user=NATS_USER, password=NATS_PASS):
    """Return a connected NATS client."""
    if nats is None:
        raise RuntimeError("nats-py not installed")
    nc = await nats.connect(
        url,
        user=user,
        password=password,
        connect_timeout=5,
        reconnect_time_wait=2,
        max_reconnect_attempts=10,
    )
    return nc


async def subscribe(nc, subject, cb):
    """Subscribe to a NATS subject with a callback."""
    return await nc.subscribe(subject, cb=cb)


async def publish(nc, subject, payload: bytes):
    """Publish bytes to a NATS subject."""
    await nc.publish(subject, payload)

