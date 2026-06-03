import os, glob, re

replacements = [
    # Distribution Centers
    (r'\b5 DCs\b', '4 DCs'),
    (r'\b5-DC\b', '4-DC'),
    (r'\b5 regional DCs\b', '4 regional DCs'),
    (r'\bfive distribution centers\b', 'four distribution centers'),
    (r'\b5 distribution centers\b', '4 distribution centers'),
    (r'\b5 WMS\b', '4 WMS'),
    (r'205 locations \(200 stores \+ 5 DCs\)', '204 locations (200 stores + 4 DCs)'),
    (r'200 stores \+ 5 DCs', '200 stores + 4 DCs'),
    (r'5 DC operating accounts', '4 DC operating accounts'),
    (r'\b5 DCs ×', '4 DCs ×'),
    (r'5 mega-DCs', '4 mega-DCs'),

    # POS Terminals
    (r'\b1,000 POS\b', '600 POS'),
    (r'\b1000 POS\b', '600 POS'),
    (r'\b5 per store\b', '3 per store'),
    (r'\b5 POS terminals\b', '3 POS terminals'),
    (r'\b5 POS\b', '3 POS'),
    (r'3 of 5 POS', '2 of 3 POS'),
    (r'1,000–1,500', '600–1,100'),
    (r'5 handles ~467', '3 handles ~467'),
    (r'Covers 5 POS', 'Covers 3 POS'),
    (r'1K\+ terminals', '600+ terminals'),

    # Staffing / Personnel
    (r'\b6,000 \(30 per store\)', '5,600 (28 per store)'),
    (r'\b30 per store\b', '28 per store'),
    (r'30 vs\. Wilcon', '28 vs. Wilcon'),
    (r'35 to 30', '30 to 28'),
    (r'\~750 \(5 DCs × \~150\)', '~600 (4 DCs × ~150)'),
    (r'\~750 total\b', '~600 total'),
    (r'\bCashiers \| 6\b', 'Cashiers | 4'),

    # Headcount Totals
    (r'\b7,050\b', '6,510'),
    (r'\b7050\b', '6510'),
    (r'\b7,060\b', '6,510'),
    (r'\b7060\b', '6510'),
    (r'\b7,070\b', '6,520'),
    (r'\b7070\b', '6520'),
]

for filepath in glob.glob('/home/riddler/erp_eval/**/*.md', recursive=True):
    with open(filepath, 'r') as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements:
        new_content = re.sub(old, new, new_content)
        
    if content != new_content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")

