"""شمارش کامل زیرگراف‌های مثال؛ کنترل مستقل، نه پیاده‌سازی مقیاس‌پذیر gSpan
Run: python chapter_02/example_2_5_2_frequent_subgraphs.py

"""
"""Exhaustive check of the book example, not a gSpan implementation.

Occurrences are distinct nonempty connected edge subsets, not vertex mappings.
Only Python's standard library is required.
"""
from itertools import combinations, permutations
from collections import Counter

edges = ((0, 1), (1, 2), (1, 3), (2, 4))

def canonical(subset):
    vertices = sorted({v for edge in subset for v in edge})
    reached = {vertices[0]}
    while True:
        expanded = reached | {v for edge in subset if reached.intersection(edge)
                              for v in edge}
        if expanded == reached:
            break
        reached = expanded
    if reached != set(vertices):
        return None
    edge_set = {frozenset(edge) for edge in subset}
    # All adjacency strings under vertex permutations: a complete isomorphism test.
    code = min(tuple(int(frozenset((order[i], order[j])) in edge_set)
                     for i in range(len(order)) for j in range(i + 1, len(order)))
               for order in permutations(vertices))
    return len(vertices), code

counts = Counter()
for size in range(1, len(edges) + 1):
    for subset in combinations(edges, size):
        key = canonical(subset)
        if key is not None:
            counts[key] += 1

representatives = {
    'K2': ((0, 1),),
    'P3': ((0, 1), (1, 2)),
    'P4': ((0, 1), (1, 2), (2, 4)),
    'K1,3': ((0, 1), (1, 2), (1, 3)),
    'whole tree': edges,
}
actual = {name: counts[canonical(subset)] for name, subset in representatives.items()}
assert len(counts) == 5
assert actual == {'K2': 4, 'P3': 4, 'P4': 2, 'K1,3': 1, 'whole tree': 1}
assert sum(counts.values()) == 12
for name, count in actual.items():
    print(f'{name}: {count} edge-subset occurrences; transactional support = 1')
print('Verified: 15 nonempty edge subsets, 12 connected occurrences, 5 patterns.')
