import copy
#stores the state of the image
class ImageMemento:
    def __init__(self, image, description):
        self._image = copy.deepcopy(image)
        self._description = description

    def get_image(self):
        return self._image

    def get_description(self):
        return self._description
    
#Manages memento history and provides methods to undo and redo changes.
class ImageCaretaker:
    def __init__(self):
        self.mementos = []
        self.current_index = -1

    def add_memento(self, memento):
        self.mementos = self.mementos[:self.current_index + 1]
        self.mementos.append(memento)
        self.current_index += 1

    def get_undo(self):
        if self.current_index >= 0:
            self.current_index -= 1
            return self.mementos[self.current_index]
        return None

    def get_redo(self):
        if self.current_index < len(self.mementos) - 1:
            self.current_index += 1
            return self.mementos[self.current_index]
        return None