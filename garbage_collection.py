
import gc
import tracemalloc

def create_objects():
    objects = []
    for i in range(1000):
        item = {}
        item['id'] = i
        item['self'] = item
        objects.append(item)
    return objects

tracemalloc.start()
gc.collect()
before = tracemalloc.get_traced_memory()[0]
print('Memory before creating objects:', before, 'bytes')

data = create_objects()
current = tracemalloc.get_traced_memory()[0]
print('Memory after creating objects:', current, 'bytes')

del data
before_gc = tracemalloc.get_traced_memory()[0]
print('Memory before manual garbage collection:', before_gc, 'bytes')

gc.set_debug(gc.DEBUG_STATS)
collected = gc.collect()
gc.set_debug(0)

after = tracemalloc.get_traced_memory()[0]
print('Objects collected:', collected)
print('Memory after garbage collection:', after, 'bytes')
