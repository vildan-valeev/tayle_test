"""
Тестовая проверка алгоритма перевода денег со счетов (на работу django не влияет...)
"""

from django.test import TestCase


def transaction_example(need: int, bills: list) -> list:
    """Имитация снятия денег со счетов"""
    # счет с минимальным остатком
    m_bill = min(bills)
    # минимально равные доли которые можно снимать
    m_need = need / len(bills)
    print(m_need, m_bill)
    if m_bill >= m_need:
        return [i - m_need for i in bills]
    return bills


class TestTransaction(TestCase):

    def test_t_1(self):
        """Недостаточно"""

        need = 450
        # У всех должно было сняться по 150, но т.к. первый счет меньше 150, транзакция остановлена -
        # по условиям - со всех счетов должна списываться одинаковая сумма.
        # Максимальный счет списания здесь 300р
        bills = [100, 200, 200]
        after_transaction = [100, 200, 200]
        self.assertEqual(transaction_example(need, bills), after_transaction, 'example #1')

    def test_t_2(self):
        """Достаточно"""
        need = 300
        bills = [100, 100, 100]
        after_transaction = [0, 0, 0]
        self.assertEqual(transaction_example(need, bills), after_transaction, 'example #2')

    def test_t_3(self):
        """Недостаточно"""
        need = 300
        bills = [0, 0, 400]
        after_transaction = [0, 0, 400]
        self.assertEqual(transaction_example(need, bills), after_transaction, 'example #3')

    def test_t_4(self):
        """Достаточно средств"""
        need = 600
        bills = [300, 400, 500]
        after_transaction = [100, 200, 300]
        self.assertEqual(transaction_example(need, bills), after_transaction, 'example #4')
