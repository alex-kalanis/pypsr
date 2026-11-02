from ..logger import EnumLevelsAdapter, LogLevel


class TestLogLevel:

    def test_level_number(self) -> None:
        assert 7 == EnumLevelsAdapter.level_to_number(LogLevel.DEBUG)

    def test_number_level(self) -> None:
        assert LogLevel.DEBUG == EnumLevelsAdapter.number_to_level(7)

    def test_number_level_invalid(self) -> None:
        assert LogLevel.ERROR == EnumLevelsAdapter.number_to_level(99)

    def test_level_short(self) -> None:
        assert 'crit' == EnumLevelsAdapter.level_to_short(LogLevel.CRITICAL)

    def test_short_level(self) -> None:
        assert LogLevel.CRITICAL == EnumLevelsAdapter.short_to_level('crit')

    def test_short_level_invalid(self) -> None:
        assert LogLevel.ERROR == EnumLevelsAdapter.short_to_level('nope')
