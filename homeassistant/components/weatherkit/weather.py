"""Support for the Apple WeatherKit Service."""

# from __future__ import annotations

# from statistics import mean
# from typing import Any, cast

# from homeassistant.components.weather import (
#     ATTR_FORECAST_CONDITION,
#     ATTR_FORECAST_NATIVE_PRECIPITATION,
#     ATTR_FORECAST_NATIVE_TEMP,
#     ATTR_FORECAST_NATIVE_TEMP_LOW,
#     ATTR_FORECAST_NATIVE_WIND_SPEED,
#     ATTR_FORECAST_PRECIPITATION_PROBABILITY,
#     ATTR_FORECAST_TIME,
#     ATTR_FORECAST_WIND_BEARING,
#     Forecast,
#     WeatherEntity,
# )
# from homeassistant.config_entries import ConfigEntry
# from homeassistant.const import (
#     UnitOfLength,
#     UnitOfPrecipitationDepth,
#     UnitOfPressure,
#     UnitOfSpeed,
#     UnitOfTemperature,
# )
# from homeassistant.core import HomeAssistant
# from homeassistant.helpers.entity_platform import AddEntitiesCallback
# from homeassistant.helpers.update_coordinator import CoordinatorEntity
# from homeassistant.util.dt import utc_from_timestamp
