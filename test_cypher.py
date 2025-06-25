from cypher import encrypt, match

class TestEncrypt():
    def test_case1(self):
        assert encrypt('Debopam') == 'Efcpqbn'

    def test_case2(self):
        assert encrypt('Debopam', 5) != 'Efcpqbn'

class TestMatch():
    def test_case1(self):
        assert match('Efcpqbn', 'Debopam', 1)

    def test_case2(self):
        assert not match('Efcpqbn', 'Debopam', 2)