from TestsLab567.testCRUD import testAdaugaObiect, testStergeObiect, testModificaObiect
from TestsLab567.testDomain import testObiect
from TestsLab567.testFunctionalitati import testMutareObiect, testConcatenareString, testCelMaiMarePretPerLocatie, testOrdonareDupaPret, testSumaPreturilorPerAn


def runAllTests():

    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testModificaObiect()
    testMutareObiect()
    testConcatenareString()
    testCelMaiMarePretPerLocatie()
    testOrdonareDupaPret()
    testSumaPreturilorPerAn()
