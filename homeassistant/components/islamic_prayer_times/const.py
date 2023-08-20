"""Constants for the Islamic Prayer component."""
from typing import Final

DOMAIN: Final = "islamic_prayer_times"
NAME: Final = "Islamic Prayer Times"

CONF_CALC_METHOD: Final = "calculation_method"
CALC_METHODS: list[str] = [
    "jafari",
    "karachi",
    "isna",
    "mwl",
    "makkah",
    "egypt",
    "tehran",
    "gulf",
    "kuwait",
    "qatar",
    "singapore",
    "france",
    "turkey",
    "russia",
    "moonsighting",
    "custom",
]
DEFAULT_CALC_METHOD: Final = "isna"

CONF_LAT_ADJ_METHOD: Final = "latitude_adjustment_method"
LAT_ADJ_METHODS: list[str] = ["middle of the night", "one seventh", "angle based"]
DEFAULT_LAT_ADJ_METHOD: Final = "middle of the night"

CONF_MIDNIGHT_MODE: Final = "midnight_mode"
MIDNIGHT_MODES: list[str] = ["standard", "jafari"]
DEFAULT_MIDNIGHT_MODE: Final = "standard"

CONF_SCHOOL: Final = "school"
SCHOOLS: list[str] = ["shafi", "hanafi"]
DEFAULT_SCHOOL: Final = "shafi"
