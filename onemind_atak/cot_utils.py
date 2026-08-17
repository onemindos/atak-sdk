"""
CoT (Cursor on Target) XML utilities — shared across all plugins.
Build and parse CoT messages for TAK Server 5.7.
"""
import xml.etree.ElementTree as ET
from datetime import datetime, timezone


def now_cot() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.00Z")


def build_cot(uid: str, lat: float, lon: float, hae: float = 0.0,
              cot_type: str = "a-f-G-U-C", callsign: str = "ONEMIND") -> str:
    """Build a minimal CoT XML string."""
    now = now_cot()
    root = ET.Element("event", {
        "version": "2.0",
        "uid": uid,
        "type": cot_type,
        "time": now,
        "start": now,
        "stale": now,
        "how": "m-g",
    })
    ET.SubElement(root, "point", {
        "lat": str(lat), "lon": str(lon),
        "hae": str(hae), "ce": "9999999.0", "le": "9999999.0"
    })
    detail = ET.SubElement(root, "detail")
    ET.SubElement(detail, "contact", {"callsign": callsign})
    return ET.tostring(root, encoding="unicode")


def parse_cot(xml_str: str) -> dict:
    """Parse a CoT XML string into a dict."""
    root = ET.fromstring(xml_str)
    pt = root.find("point")
    detail = root.find("detail")
    contact = detail.find("contact") if detail is not None else None
    return {
        "uid": root.get("uid"),
        "type": root.get("type"),
        "lat": float(pt.get("lat", 0)) if pt is not None else 0,
        "lon": float(pt.get("lon", 0)) if pt is not None else 0,
        "hae": float(pt.get("hae", 0)) if pt is not None else 0,
        "callsign": contact.get("callsign") if contact is not None else "",
    }

