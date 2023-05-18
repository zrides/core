"""Weather data coordinator for the Apple WeatherKit service."""

import logging

import async_timeout

# import forecastio
# from forecastio.models import Forecast
import requests

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

ATTRIBUTION = "Powered by Apple Weather"


class WeatherUpdateCoordinator(DataUpdateCoordinator):
    """Weather data update coordinator."""

    def __init__(
        self,
        api_key,
        latitude,
        longitude,
        countryCode,
        scan_int,
        hass: HomeAssistant,
    ) -> None:
        """Initialize coordinator."""
        self._api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.country_code = countryCode
        self.scan_int = scan_int
        self.requested_units = "si"

        self.data = None
        self.currently = None
        self.hourly = None
        self.daily = None
        self._connect_error = False

        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=scan_int)

    async def _async_update_data(self):
        """Update the data."""
        data = {}
        async with async_timeout.timeout(30):
            try:
                data = await self._get_weather()
            except Exception as error:
                raise UpdateFailed(error) from error
        return data

    async def _get_weather(self):
        """Poll weather data from Weatherkit."""

        language = "en-us"

        headers = {"Authorization": f"Bearer {self._api_key}"}
        payload = {
            "countryCode": f"{self.country_code}",
            "dataSets": "currentWeather,forecastDaily,forecastHourly,forecastNextHour,weatherAlerts",
            "timezone": "US/New_York",
        }

        forecast_string = (
            "https://weatherkit.apple.com/api/v1/weather/"
            + language
            + "/"
            + str(self.latitude)
            + "/"
            + str(self.longitude)
        )

        r_data = requests.get(
            forecast_string, params=payload, headers=headers, timeout=10
        )
        json_forecast = r_data.json()

        return json_forecast
