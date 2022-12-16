from source.WineValidation import *

def test_isFixedAcidityValid():
    assert(isFixedAcidityValid(15.0) is True)

def test_isFixedAcidityInvalid():
    assert(isFixedAcidityValid(40.0) is False)

def test_isVolatileAcidityValid():
    assert(isVolatileAcidityValid(1.5) is True)

def test_isVolatileAcidityInvalid():
    assert(isVolatileAcidityValid(4.0) is False)

def test_isCitricAcidValid():
    assert(isCitricAcidValid(0.5) is True)

def test_isCitricAcidInvalid():
    assert(isCitricAcidValid(2.0) is False)

def test_isResidualSugarValid():
    assert(isResidualSugarValid(15.0) is True)

def test_isResidualSugarInvalid():
    assert(isResidualSugarValid(40.0) is False)

def test_isChloridesValid():
    assert(isChloridesValid(0.5) is True)

def test_isChloridesInvalid():
    assert(isChloridesValid(2.0) is False)

def test_isFreeSulfurDioxydeValid():
    assert(isFreeSulfurDioxydeValid(100.0) is True)

def test_isFreeSulfurDioxydeInvalid():
    assert(isFreeSulfurDioxydeValid(210.0) is False)

def test_isTotalSulfurDioxydeValid():
    assert(isTotalSulfurDioxydeValid(150.0) is True)

def test_isTotalSulfurDioxydeInvalid():
    assert(isTotalSulfurDioxydeValid(0.0) is False)

def test_isDensityValid():
    assert(isDensityValid(1.0) is True)

def test_isDensityInvalid():
    assert(isDensityValid(0.9) is False)

def test_isPHValid():
    assert(isPHValid(3.0) is True)

def test_isPHInvalid():
    assert(isPHValid(0.0) is False)

def test_isSulphatesValid():
    assert(isSulphatesValid(1.5) is True)

def test_isSulphatesInvalid():
    assert(isSulphatesValid(5.0) is False)

def test_isAlcoholValid():
    assert(isAlcoholValid(7.5) is True)

def test_isAlcoholInvalid():
    assert(isAlcoholValid(20.0) is False)

def test_isQualityValid():
    assert(isQualityValid(5) is True)

def test_isQualityInvalid():
    assert(isQualityValid(12) is False)    

def test_validWine():
    assert(isWineValid(15, 1.5, 0.5, 15, 0.5, 100, 150, 1.0, 3.0, 1.5, 7.5) is True)

def test_validWineWithQuality():
    assert(isWineValidWithQuality(15, 1.5, 0.5, 15, 0.5, 100, 150, 1.0, 3.0, 1.5, 7.5, 5) is True)

def test_invalidWineOnSulfurDioxyde():
    assert(isWineValid(15, 1.5, 0.5, 15, 0.5, 150, 100, 1.0, 3.0, 1.5, 7.5) is False)

