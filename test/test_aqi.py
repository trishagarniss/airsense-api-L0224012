import pytest

from aqi import kategori_pm25


@pytest.mark.parametrize("nilai, harapan", [
    (10, "baik"), (15.5, "baik"), (40, "sedang"),
    (100, "tidak sehat"), (200, "sangat tidak sehat"),
])
def test_kategori(nilai, harapan):
    assert kategori_pm25(nilai) == harapan


def test_negatif_ditolak():
    with pytest.raises(ValueError):
        kategori_pm25(-1)