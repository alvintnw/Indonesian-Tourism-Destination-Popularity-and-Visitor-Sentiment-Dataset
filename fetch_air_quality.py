from datetime import datetime, timedelta
import numpy as np
import pandas as pd


def generate_air_quality_dataset():
  np.random.seed(303)
  n_rows = 1200

  cities_data = [
      {"city": "Jakarta Pusat", "province": "DKI Jakarta"},
      {"city": "Surabaya", "province": "Jawa Timur"},
      {"city": "Bandung", "province": "Jawa Barat"},
      {"city": "Medan", "province": "Sumatera Utara"},
      {"city": "Semarang", "province": "Jawa Tengah"},
      {"city": "Makassar", "province": "Sulawesi Selatan"},
      {"city": "Tangerang", "province": "Banten"},
      {"city": "Bekasi", "province": "Jawa Barat"},
      {"city": "Depok", "province": "Jawa Barat"},
      {"city": "Palembang", "province": "Sumatera Selatan"},
  ]

  end_date = datetime.now()
  start_date = end_date - timedelta(days=30)
  date_list = [
      start_date + timedelta(hours=int(np.random.randint(0, 720)))
      for _ in range(n_rows)
  ]

  pollutants = ["PM2.5", "PM10", "CO", "NO2"]

  data = []
  for i in range(n_rows):
    loc = np.random.choice(cities_data)
    city = loc["city"]
    province = loc["province"]

    # Simulasi kadar polutan dan AQI
    pm25 = round(float(np.random.uniform(15.0, 110.0)), 1)
    pm10 = round(float(pm25 * np.random.uniform(1.2, 1.8)), 1)
    co = round(float(np.random.uniform(0.5, 3.5)), 2)
    no2 = round(float(np.random.uniform(10.0, 55.0)), 1)

    # Estimasi AQI berdasarkan PM2.5
    aqi = int(pm25 * np.random.uniform(1.1, 1.4))

    if aqi <= 50:
      status = "Good"
    elif aqi <= 100:
      status = "Moderate"
    elif aqi <= 150:
      status = "Unhealthy for Sensitive Groups"
    else:
      status = "Unhealthy"

    dominant = np.random.choice(
        pollutants, p=[0.55, 0.25, 0.10, 0.10]
    )

    data.append({
        "record_id": f"AQI-{8000 + i}",
        "timestamp": date_list[i].strftime("%Y-%m-%d %H:%M"),
        "city": city,
        "province": province,
        "pm25_ug_m3": pm25,
        "pm10_ug_m3": pm10,
        "co_ppm": co,
        "no2_ppb": no2,
        "aqi_score": aqi,
        "air_quality_status": status,
        "dominant_pollutant": dominant,
    })

  df = pd.DataFrame(data)
  filename = "indonesia_air_quality_health.csv"
  df.to_csv(filename, index=False)
  print(
      f"Success! Dataset generated with {len(df)} records and saved as"
      f" '{filename}'"
  )


if __name__ == "__main__":
  generate_air_quality_dataset()
