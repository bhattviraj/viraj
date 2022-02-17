import unittest
import pytest
import time
from testCases.test_03todo import Test_003_DDT_AddTodo
from testCases.test_postjob import Test_0008_postJob
from utilities.customLogger import LogGen

tc1=unittest.TestLoader().loadTestsFromTestCase(Test_003_DDT_AddTodo)
tc2=unittest.TestLoader().loadTestsFromTestCase(Test_0008_postJob)

sanityTestSuite = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run()