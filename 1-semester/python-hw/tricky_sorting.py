items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]
# хотим отсортировать этот список по последней букве второго элемента каждого tuple
sorted_items_required = [('string', 'a'), ('one', 'two'), ('three', 'four'), ('five', 'six')]

sorted_items = sorted(items, key=lambda x: x[1][-1])
print(sorted_items)