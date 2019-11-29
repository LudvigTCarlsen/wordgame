import unittest
import functions
import socket
class test_server(unittest.TestCase):
    HOST = '127.0.0.1'
    PORT = 12345
    global s
    
    def test_gen_ord(self):
        word1 = functions.gen_random_ord()
        word2 = functions.gen_random_ord()
        self.assertNotEqual(word1, word2)

    def test_hints(self):
        testvalues = ['polis','polka']
        for testValue in testvalues:
            with self.subTest(status_code=testValue):
                test = functions.hints(testValue, 'polsk')
                testvalues = (test[25], test[51])
                actualvalues = ('3','1')
                self.assertEqual(testvalues, actualvalues)

    def test_playername_format(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST,self.PORT))
            this_client_name = '#%&ludvig'
            s.sendall(this_client_name.encode('utf-8'))
            data = s.recv(1024).decode('utf-8')
            s.sendall('quitting'.encode('utf-8'))

        self.assertEqual(this_client_name, data)

     
if __name__ == "__main__":
    unittest.main()