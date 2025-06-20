import unittest
from unittest.mock import patch
from core.scanner import PortScanner

class TestPortScanner(unittest.TestCase):
    
    @patch('socket.socket')
    def test_scan_open_port(self, mock_socket):
        mock_socket.return_value.connect_ex.return_value = 0
        scanner = PortScanner("127.0.0.1")
        result = scanner.scan_port(80)
        self.assertEqual(result["port"], 80)
        self.assertEqual(result["status"], "open")

if __name__ == "__main__":
    unittest.main()
