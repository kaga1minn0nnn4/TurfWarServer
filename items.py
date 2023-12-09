from item_template import ItemTemplate

class VerticalPaintItem(ItemTemplate):
    def __init__(self) -> None:
        super().__init__()

        self.paint_area = [ \
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0]
        ]

        self.item_no = 0

class HorizontalPaintItem(ItemTemplate):
    def __init__(self) -> None:
        super().__init__()

        self.paint_area = [ \
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        self.item_no = 1

class DiagonalCrossPaintItem(ItemTemplate):
    def __init__(self) -> None:
        super().__init__()

        self.paint_area = [ \
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1]
        ]

        self.item_no = 2

class CrossPaintItem(ItemTemplate):
    def __init__(self) -> None:
        super().__init__()

        self.paint_area = [ \
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0]
        ]

        self.item_no = 3

class SaikyoPaintItem(ItemTemplate):
    def __init__(self) -> None:
        super().__init__()

        self.paint_area = [ \
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]

        self.item_no = 4
