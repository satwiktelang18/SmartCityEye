class ObjectCounter:

    def __init__(self):

        self.objects = {}

    def add(self, object_id, class_name):

        if object_id not in self.objects:
            self.objects[object_id] = class_name

    def counts(self):

        result = {}

        for cls in self.objects.values():

            result[cls] = result.get(cls, 0) + 1

        return result

    def total(self):

        return len(self.objects)