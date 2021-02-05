import postitoimipaikka

POSTINUMEROT = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}

ERIKOISTAPAUKSET = {
    "43800": "KIVIJÄRVI",
    "91150": "YLI-OLHAVA",
    "65374": "SMART POST",
    "90210": "BEVERLY HILLS"
}


def test_helsingin_postinumero():
    tulos = postitoimipaikka.etsi_toimipaikka('00100')

    assert tulos == "HELSINKI"


def test_korvatunturin_postinumero():
    tulos = postitoimipaikka.etsi_toimipaikka('99999')

    assert tulos == "KORVATUNTURI"


def test_postinumero_jota_ei_loydy():
    tulos = postitoimipaikka.etsi_toimipaikka('1')

    assert tulos == "Tuntematon"


def test_postinumerot_omalla_datalla(mocker):
    oma_data = ERIKOISTAPAUKSET
    mocker.patch('http_pyynto.hae_postinumerot', return_value=oma_data)

    tulos = postitoimipaikka.etsi_toimipaikka('90210')

    assert tulos == 'BEVERLY HILLS'
