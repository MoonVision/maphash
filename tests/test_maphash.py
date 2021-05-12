from maphash import maphash


def test_maphash_hashes_int():
    assert (
        maphash(1) == "67b176705b46206614219f47a05aee7ae6a3edbe850bbbe214c536b989aea4d2"
    )


def test_maphash_hashes_float():
    assert (
        maphash(0.1)
        == "75bd59c8426679f3ef7b3a37184ee08e2e5ecee840e330acf6782d77cf2a2d1b"
    )


def test_maphash_hashes_str():
    assert (
        maphash("string")
        == "00ff5fd099f3820fa1196c77d97331caaec09301635641a113b1b81d268b26df"
    )


def test_maphash_hashes_dict():
    assert (
        maphash(dict())
        == "840eb7aa2a9935de63366bacbe9d97e978a859e93dc792a0334de60ed52f8e99"
    )


def test_maphash_hashes_list():
    assert (
        maphash(list())
        == "ca4510738395af1429224dd785675309c344b2b549632e20275c69b15ed1d210"
    )


def test_maphash_hashes_none():
    assert (
        maphash(None)
        == "3ea445410f608e6453cdcb7dbe42d57a89aca018993d7e87da85993cbccc6308"
    )
