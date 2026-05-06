# Daily Weather Report – Setup Guide

## What this does
Runs every morning at 08:00, fetches weather for Stockholm, Gothenburg and Malmö
from the free Open-Meteo API (no key needed), and appends a formatted report to
`weather_log.txt` in the same folder as the script.

---

## 1. Prerequisites

```bash
# Python 3.10+ is required (no extra packages needed — only stdlib + urllib)
python3 --version
```

---

## 2. Schedule on Linux / macOS — cron

```bash
# Open your crontab
crontab -e

# Add this line (adjust the path to wherever you saved weather_report.py)
0 8 * * * /usr/bin/python3 /path/to/weather_report.py >> /path/to/cron.log 2>&1
```

Cron syntax quick reference:
```
┌─ minute  (0–59)
│ ┌─ hour    (0–23)
│ │ ┌─ day of month (1–31)
│ │ │ ┌─ month (1–12)
│ │ │ │ ┌─ day of week (0–7, 0=Sun)
│ │ │ │ │
0 8 * * *   ← every day at 08:00
```

Verify it was saved:
```bash
crontab -l
```

---

## 3. Schedule on Windows — Task Scheduler

### Option A: via the GUI
1. Open **Task Scheduler** (search in Start menu)
2. Click **Create Basic Task…**
3. Name it "Daily Weather Report"
4. Trigger → **Daily**, start time **08:00**
5. Action → **Start a program**
   - Program: `C:\Python312\python.exe`  (or wherever Python is installed)
   - Arguments: `C:\path\to\weather_report.py`
6. Finish → **OK**

### Option B: via PowerShell (one command)
```powershell
$action  = New-ScheduledTaskAction -Execute "python.exe" -Argument "C:\path\to\weather_report.py"
$trigger = New-ScheduledTaskTrigger -Daily -At "08:00"
Register-ScheduledTask -TaskName "DailyWeatherReport" -Action $action -Trigger $trigger -RunLevel Highest
```

---

## 4. (Bonus) Enable email delivery

Edit `weather_report.py` and set:

```python
EMAIL_ENABLED  = True
EMAIL_SENDER   = "you@gmail.com"
EMAIL_PASSWORD = "xxxx xxxx xxxx xxxx"   # Gmail App Password
EMAIL_RECEIVER = "you@gmail.com"
```

### How to create a Gmail App Password
1. Go to https://myaccount.google.com/security
2. Enable **2-Step Verification** if not already on
3. Search for **App passwords** → create one for "Mail / Windows/Mac/Linux"
4. Paste the 16-character password into `EMAIL_PASSWORD`

---

## 5. Test it manually

```bash
python3 weather_report.py
```

Check the log:
```bash
cat weather_log.txt
```

---

## 6. Sample output

```
==========================================================
  🌍  DAILY WEATHER REPORT
  Wednesday, 06 May 2026  –  generated at 08:00
==========================================================

  📍 Stockholm
     Conditions   : ⛅  Partly cloudy
     Temperature  : 14°C  (feels like 12°C)
     Precipitation: 0.0 mm
     Wind speed   : 4.2 m/s

  📍 Gothenburg
     Conditions   : 🌧️  Slight rain
     Temperature  : 11°C  (feels like 9°C)
     Precipitation: 1.2 mm
     Wind speed   : 6.8 m/s

  📍 Malmö
     Conditions   : 🌦️  Light drizzle
     Temperature  : 13°C  (feels like 11°C)
     Precipitation: 0.4 mm
     Wind speed   : 5.1 m/s

==========================================================
```

---

## File structure

```
your-folder/
├── weather_report.py   ← the script
├── weather_log.txt     ← appended every run (created automatically)
└── README.md           ← this file
```
