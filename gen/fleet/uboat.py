import random

from dcs.ships import U_boat_VIIC_U_flak

from gen.sam.group_generator import ShipGroupGenerator


class UBoatGroupGenerator(ShipGroupGenerator):
    def generate(self):

        for i in range(random.randint(1, 4)):
            self.add_unit(
                U_boat_VIIC_U_flak,
                "Uboat" + str(i),
                self.position.x + i * random.randint(100, 250),
                self.position.y + (random.randint(100, 200) - 100),
                self.heading,
            )

        self.get_generated_group().points[0].speed = 20
