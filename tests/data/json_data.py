GETAccounts_response = {'accounts': [{'id': '101-011-6557245-001', 'tags': []}]}

GETAccountID_response = {
    'account': {'id': '101-011-6557245-001', 'createdTime': '2017-08-11T15:04:31.639182352Z', 'currency': 'AUD',
                'createdByUserID': 6557245, 'alias': 'Primary', 'marginRate': '0.02', 'hedgingEnabled': False,
                'lastTransactionID': '14', 'balance': '99999.9138', 'openTradeCount': 0, 'openPositionCount': 0,
                'pendingOrderCount': 0, 'pl': '-0.0769', 'resettablePL': '-0.0769', 'financing': '-0.0093',
                'commission': '0.0000', 'orders': [], 'positions': [{'instrument': 'EUR_USD',
                                                                     'long': {'units': '0', 'pl': '-0.0769',
                                                                              'resettablePL': '-0.0769',
                                                                              'financing': '-0.0093',
                                                                              'unrealizedPL': '0.0000'},
                                                                     'short': {'units': '0', 'pl': '0.0000',
                                                                               'resettablePL': '0.0000',
                                                                               'financing': '0.0000',
                                                                               'unrealizedPL': '0.0000'},
                                                                     'pl': '-0.0769', 'resettablePL': '-0.0769',
                                                                     'financing': '-0.0093', 'commission': '0.0000',
                                                                     'unrealizedPL': '0.0000'}], 'trades': [],
                'unrealizedPL': '0.0000', 'NAV': '99999.9138', 'marginUsed': '0.0000', 'marginAvailable': '99999.9138',
                'positionValue': '0.0000', 'marginCloseoutUnrealizedPL': '0.0000', 'marginCloseoutNAV': '99999.9138',
                'marginCloseoutMarginUsed': '0.0000', 'marginCloseoutPositionValue': '0.0000',
                'marginCloseoutPercent': '0.00000', 'withdrawalLimit': '99999.9138', 'marginCallMarginUsed': '0.0000',
                'marginCallPercent': '0.00000'}, 'lastTransactionID': '14'}

GETAccountIDSummary_response = {
    'account': {'id': '101-011-6557245-001', 'createdTime': '2017-08-11T15:04:31.639182352Z', 'currency': 'AUD',
                'createdByUserID': 6557245, 'alias': 'Primary', 'marginRate': '0.02', 'hedgingEnabled': False,
                'lastTransactionID': '56', 'balance': '100000.1795', 'openTradeCount': 2, 'openPositionCount': 1,
                'pendingOrderCount': 0, 'pl': '0.1899', 'resettablePL': '0.1899', 'financing': '-0.0104',
                'commission': '0.0000', 'unrealizedPL': '0.0033', 'NAV': '100000.1828', 'marginUsed': '0.0401',
                'marginAvailable': '100000.1427', 'positionValue': '2.0027', 'marginCloseoutUnrealizedPL': '0.0046',
                'marginCloseoutNAV': '100000.1841', 'marginCloseoutMarginUsed': '0.0400',
                'marginCloseoutPositionValue': '2.0000', 'marginCloseoutPercent': '0.00000',
                'withdrawalLimit': '100000.1427', 'marginCallMarginUsed': '0.0400', 'marginCallPercent': '0.00000'},
    'lastTransactionID': '56'}
