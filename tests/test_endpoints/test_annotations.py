import random

import pytest

from async_v20.endpoints import annotations


def test_count_only_allows_valid_data():
    with pytest.raises(ValueError):
        annotations.Count(0)

    with pytest.raises(ValueError):
        annotations.Count(5001)

    assert annotations.Count(random.randrange(1, 5001))

    assert int(annotations.Count()) == 500


def test_daily_alignment_only_allows_valid_data():
    with pytest.raises(ValueError):
        annotations.DailyAlignment(-1)

    with pytest.raises(ValueError):
        annotations.DailyAlignment(24)

    assert annotations.Count(random.randrange(24))

    assert int(annotations.DailyAlignment()) == 17


def test_alignment_time_zone_only_allows_valid_data():
    assert annotations.AlignmentTimezone() == 'America/New_York'

def test_smooth_returns_correct_default_data():
    assert annotations.Smooth() == 'False'
