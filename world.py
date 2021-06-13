from platformPiece import platformPiece


class World:
    def __init__(self):
        pass

    def platformer(self, image, x_pos, y_pos, loopControl, axs, group):
        # axs determines which axis we add
        # loopControl determines how many to add
        control = 0
        if axs:
            self.stp = x_pos
            while control < loopControl:
                platform = platformPiece(image, self.stp, y_pos)
                group.add(platform)
                self.stp += 10
                control += 1
        else:
            self.stp = y_pos
            while control < loopControl:
                platform = platformPiece(image, x_pos, self.stp)
                group.add(platform)
                self.stp += 15
                control += 1
