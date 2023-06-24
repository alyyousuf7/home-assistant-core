"""Constants for the Islamic Prayer component."""
from typing import Final

from prayer_times_calculator import PrayerTimesCalculator

DOMAIN: Final = "islamic_prayer_times"
NAME: Final = "Islamic Prayer Times"

CONF_CALC_METHOD: Final = "calculation_method"
CALC_METHODS: list[str] = list(PrayerTimesCalculator.CALCULATION_METHODS)
DEFAULT_CALC_METHOD: Final = "isna"

CONF_LAT_ADJ_METHOD: Final = "latitude_adjustment_method"
LAT_ADJ_METHODS: list[str] = [
    # PrayerTimesCalculator.LAT_ADJ_METHODS has values with space in them,
    # which goes against translation_key requirement
    value.replace(" ", "_")
    for value in list(PrayerTimesCalculator.LAT_ADJ_METHODS)
]
DEFAULT_LAT_ADJ_METHOD: Final = "middle_of_the_night"

CONF_MIDNIGHT_MODE: Final = "midnight_mode"
MIDNIGHT_MODES: list[str] = list(PrayerTimesCalculator.MIDNIGHT_MODES)
DEFAULT_MIDNIGHT_MODE: Final = "standard"

CONF_SCHOOL: Final = "school"
SCHOOLS: list[str] = list(PrayerTimesCalculator.SCHOOLS)
DEFAULT_SCHOOL: Final = "shafi"
