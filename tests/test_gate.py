import unittest
from uncertainty_gate import DynamicsEstimate, authorize

class GateTests(unittest.TestCase):
    def test_allow(self): self.assertEqual(authorize(DynamicsEstimate(.5,.1),.9),"ALLOW")
    def test_verify(self): self.assertEqual(authorize(DynamicsEstimate(.8,.2),.9),"VERIFY")
    def test_block(self): self.assertEqual(authorize(DynamicsEstimate(1.2,.1),.9),"BLOCK")
    def test_invalid_limit_and_estimate_type_rejected(self):
        with self.assertRaises(ValueError): authorize(DynamicsEstimate(.5,.1),float("nan"))
        with self.assertRaises(TypeError): authorize(None,.9)

if __name__=="__main__": unittest.main()
