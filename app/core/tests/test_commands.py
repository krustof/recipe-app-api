from unittest.mock import patch
<<<<<<< HEAD
=======

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import Test TestCase

class CommandTestx(TestCase):

    def test_wait_for_db_ready(self):
        """Test wait for DB when DB is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for DB"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.asserEqual(gi.call_count, 6)
        
>>>>>>> 182a357c770986d7a77c0c6b20f90cd0662934f3
