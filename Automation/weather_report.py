import urllib.request
import urllib.parse
import json
import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

CITIES = ["Stockholm", "Mangalore", "New Delhi"]

# Open-Meteo is free and requires no API key.
# We first geocode each city name to lat/lon, then fetch weather.
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "weather_log.txt")
EMAIL_ENABLED  = True         
EMAIL_SENDER   = "apekshashenoy.1992@gmail.com"
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")  # Use an App Password for Gmail
EMAIL_RECEIVER = "apekshashenoy.1992@gmail.com"
SMTP_HOST      = "smtp.gmail.com"
SMTP_PORT      = 587


def fetch_json(url: str) -> dict:
    """Fetch a URL and return parsed JSON."""
    with urllib.request.urlopen(url, timeout=10) as resp:
        return json.loads(resp.read().decode())


def geocode(city: str) -> tuple[float, float]:
    """Return (latitude, longitude) for a city name."""
    params = urllib.parse.urlencode({"name": city, "count": 1, "language": "en", "format": "json"})
    data = fetch_json(f"{GEOCODE_URL}?{params}")
    if not data.get("results"):
        raise ValueError(f"City not found: {city}")
    r = data["results"][0]
    return r["latitude"], r["longitude"]


def get_weather(city: str) -> dict:
    """Return a dict with current weather for the given city."""
    lat, lon = geocode(city)
    params = urllib.parse.urlencode({
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,apparent_temperature,precipitation,weathercode,windspeed_10m",
        "wind_speed_unit": "ms",
        "timezone": "auto",
    })
    data = fetch_json(f"{WEATHER_URL}?{params}")
    current = data["current"]
    return {
        "city": city,
        "temp":        current["temperature_2m"],
        "feels_like":  current["apparent_temperature"],
        "precip":      current["precipitation"],
        "wind":        current["windspeed_10m"],
        "code":        current["weathercode"],
        "time":        current["time"],
    }


# WMO Weather interpretation codes → human-readable description + emoji
WMO_CODES = {
    0: ("Clear sky", "☀️"),
    1: ("Mainly clear", "🌤️"),
    2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Foggy", "🌫️"),
    48: ("Icy fog", "🌫️"),
    51: ("Light drizzle", "🌦️"),
    53: ("Moderate drizzle", "🌦️"),
    55: ("Dense drizzle", "🌧️"),
    61: ("Slight rain", "🌧️"),
    63: ("Moderate rain", "🌧️"),
    65: ("Heavy rain", "🌧️"),
    71: ("Slight snow", "❄️"),
    73: ("Moderate snow", "❄️"),
    75: ("Heavy snow", "❄️"),
    77: ("Snow grains", "🌨️"),
    80: ("Slight showers", "🌦️"),
    81: ("Moderate showers", "🌧️"),
    82: ("Violent showers", "⛈️"),
    85: ("Slight snow showers", "🌨️"),
    86: ("Heavy snow showers", "🌨️"),
    95: ("Thunderstorm", "⛈️"),
    96: ("Thunderstorm w/ hail", "⛈️"),
    99: ("Thunderstorm w/ heavy hail", "⛈️"),
}

def describe(code: int) -> str:
    desc, emoji = WMO_CODES.get(code, ("Unknown", "❓"))
    return f"{emoji}  {desc}"


# ── Report builder ────────────────────────────────────────────────────────────

def build_report(weather_data: list[dict]) -> str:
    now   = datetime.datetime.now()
    lines = []

    lines.append("=" * 58)
    lines.append("  🌍  DAILY WEATHER REPORT")
    lines.append(f"  {now.strftime('%A, %d %B %Y  –  generated at %H:%M')}")
    lines.append("=" * 58)

    for w in weather_data:
        lines.append("")
        lines.append(f"  📍 {w['city']}")
        lines.append(f"     Conditions  : {describe(w['code'])}")
        lines.append(f"     Temperature : {w['temp']}°C  (feels like {w['feels_like']}°C)")
        lines.append(f"     Precipitation: {w['precip']} mm")
        lines.append(f"     Wind speed  : {w['wind']} m/s")

    lines.append("")
    lines.append("=" * 58)
    lines.append("")
    return "\n".join(lines)


# ── Email sender ──────────────────────────────────────────────────────────────

def send_email(subject: str, body: str) -> None:
    msg = MIMEMultipart()
    msg["From"]    = EMAIL_SENDER
    msg["To"]      = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
    print("✅  Email sent successfully.")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Fetching weather data…")

    weather_data = []
    for city in CITIES:
        try:
            data = get_weather(city)
            weather_data.append(data)
            print(f"  ✓ {city}: {data['temp']}°C, {describe(data['code'])}")
        except Exception as exc:
            print(f"  ✗ {city}: {exc}")
            weather_data.append({"city": city, "error": str(exc)})

    report = build_report([w for w in weather_data if "error" not in w])

    # Save to log file (append)
    with open(LOG_FILE, "a", encoding="utf-8") as fh:
        fh.write(report)
    print(f"📄  Report appended to {LOG_FILE}")

    # Print to console as well
    print("\n" + report)

    # Optional: send email
    if EMAIL_ENABLED:
        subject = f"🌤️ Daily Weather Report – {datetime.date.today():%d %b %Y}"
        try:
            send_email(subject, report)
        except Exception as exc:
            print(f"❌  Email failed: {exc}")


if __name__ == "__main__":
    main()
