class Stock_NoData(Exception):
    def __init__(self, token):
        super().__init__(f'No data found for stock {token}')