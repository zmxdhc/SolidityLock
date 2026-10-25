# test_soliditylock.py
"""
Tests for SolidityLock module.
"""

import unittest
from soliditylock import SolidityLock

class TestSolidityLock(unittest.TestCase):
    """Test cases for SolidityLock class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityLock()
        self.assertIsInstance(instance, SolidityLock)

    def test_run_method(self):
        """Test the run method."""
        instance = SolidityLock()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
