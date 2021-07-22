#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу


garden_set = set(garden)
meadow_set = set(meadow)
print('Садовые цветы: ', garden_set)
print('Луговые цветы: ', meadow_set)

# выведите на консоль все виды цветов

print('Все виды цветов: ' , garden_set | meadow_set)

# выведите на консоль те, которые растут и там и там

print('Цветы которые растут и там, и там', garden_set & meadow_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу

remove_set = set(garden_set & meadow_set)
end = garden_set - remove_set
print('Цветы которые растут в саду, но не растут на лугу: ', end)

# выведите на консоль те, которые растут на лугу, но не растут в саду

second_end = meadow_set - remove_set
print('Цветы которые растут на лугу, но не растут в саду: ', second_end)


