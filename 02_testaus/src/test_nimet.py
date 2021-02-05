import nimet


def test_lyhenna_j_l_runeberg():
    lyhennetty = nimet.lyhenna_nimi("Johan", "Ludvig", "Runeberg")

    assert lyhennetty == 'J. L. Runeberg'


def test_lyhenna_a_i_virtanen():
    ai_virtanen = nimet.lyhenna_nimi('Artturi', 'Ilmari', 'Virtanen')

    assert ai_virtanen == 'A. I. Virtanen'


def test_erityiset_kirjaimet():
    erikoistapaus = nimet.lyhenna_nimi('Šárka', 'Šárka', 'Kašpárková')

    assert erikoistapaus == 'Š. Š. Kašpárková'
