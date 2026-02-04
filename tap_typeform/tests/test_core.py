"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_typeform.tap import TapTypeform

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "personal_access_token": "test_token",
}

# Generate test class using SDK testing API
TestTapTypeform = get_tap_test_class(
    tap_class=TapTypeform,
    config=SAMPLE_CONFIG,
)
