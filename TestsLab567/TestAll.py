from TestsLab567.testCRUD import testAdaugaObiect, testStergeObiect, testModificaObiect, testUndoRedo, \
    testStergereUndoRedo, testModificareUndoRedo
from TestsLab567.testDomain import testObiect
from TestsLab567.testFunctionalitati import testMutareObiect, testConcatenareString, testCelMaiMarePretPerLocatie, \
    testOrdonareDupaPret, testSumaPreturilorPerAn, testMutareObiectUndoRedo, testConcatenareStringUndoRedo


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
    testUndoRedo()
    testStergereUndoRedo()
    testModificareUndoRedo()
    testMutareObiectUndoRedo()
    testConcatenareStringUndoRedo()
