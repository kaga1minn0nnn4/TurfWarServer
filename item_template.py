import random
import items

class ItemTemplate:
    def __init__(self) -> None:
        self.paint_area = []
        self.item_no = -1

    def get_mask(self, position):
        player_x = position[1]
        player_y = position[0]
        # mask = np.zeros((21, 31), dtype=np.uint8)
        mask = [[0 for j in range(31)] for i in range(21)]

        for i, row in enumerate(self.paint_area):
            for j, flag in enumerate(row):
                if flag == 0:
                    continue
                try:
                    mask[i + player_y - 2][j + player_x - 2] = 1
                except:
                    continue

        return mask

    @classmethod
    def item_from_num(cls, num):
        item_types = [
            items.VerticalPaintItem(),
            items.HorizontalPaintItem(),
            items.DiagonalCrossPaintItem(),
            items.CrossPaintItem(),
            items.SaikyoPaintItem()
        ]
        return item_types[num]

    @classmethod
    def create_random_item(cls):
        random_value = random.random()

        probabilities = [0.3, 0.25, 0.2, 0.2, 0.05]
        item_types = [
            items.VerticalPaintItem(),
            items.HorizontalPaintItem(),
            items.DiagonalCrossPaintItem(),
            items.CrossPaintItem(),
            items.SaikyoPaintItem()
        ]

        item: ItemTemplate = ItemTemplate()

        temp = 0
        for i, probability in enumerate(probabilities):
            temp += probability
            if random_value < temp:
                item = item_types[i]
                break

        return item
