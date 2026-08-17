"""
TAK Server 5.7 REST API helpers — shared across all plugins.
"""
import json
try:
    import requests
except ImportError:
    requests = None

TAK_URL  = "https://152.42.155.95:8443"
TAK_CERT = None   # Path to client cert if needed
TAK_VERIFY = False


def _session():
    if requests is None:
        raise RuntimeError("requests not installed")
    s = requests.Session()
    s.verify = TAK_VERIFY
    return s


def get_missions(base_url=TAK_URL):
    """List all missions on the TAK server."""
    s = _session()
    r = s.get(f"{base_url}/Marti/api/missions", timeout=10)
    r.raise_for_status()
    return r.json()


def post_cot(cot_xml: str, base_url=TAK_URL):
    """POST a CoT message to the TAK server injection endpoint."""
    s = _session()
    r = s.post(
        f"{base_url}/Marti/api/cot",
        data=cot_xml.encode(),
        headers={"Content-Type": "application/xml"},
        timeout=5,
    )
    r.raise_for_status()
    return r.status_code

