Already sorted list
[ (1,1), (1,2), (2,1) ]
[ (1,1), (1,2), (2,1) ]
Tests that no unnecessary swaps happen.

Reverse sorted list
[ (3,2), (2,3), (1,1) ]
[ (1,1), (2,3), (3,2) ]
Tests worst-case behavior.

Normal case – mixed shelves and orders
[ (shelf=2, order=3), (shelf=1, order=4), (shelf=2, order=1), (shelf=3, order=2) ]
[ (1,4), (2,1), (2,3), (3,2) ]
Tests standard two-key sorting.

Books with same shelf_number
[ (shelf=1, order=3), (shelf=1, order=1), (shelf=1, order=2) ]
[ (1,1), (1,2), (1,3) ]
Tests secondary-key ordering.

