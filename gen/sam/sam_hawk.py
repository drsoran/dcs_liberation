import random

from dcs.mapping import Point
from dcs.vehicles import AirDefence

from gen.sam.airdefensegroupgenerator import (
    AirDefenseRange,
    AirDefenseGroupGenerator,
)


class HawkGenerator(AirDefenseGroupGenerator):
    """
    This generate an HAWK group
    """

    name = "Hawk Site"
    price = 115

    def generate(self):
        self.add_unit(
            AirDefence.SAM_Hawk_SR__AN_MPQ_50,
            "SR",
            self.position.x + 20,
            self.position.y,
            self.heading,
        )
        self.add_unit(
            AirDefence.SAM_Hawk_Generator__PCP,
            "PCP",
            self.position.x,
            self.position.y,
            self.heading,
        )
        self.add_unit(
            AirDefence.SAM_Hawk_TR__AN_MPQ_46,
            "TR",
            self.position.x + 40,
            self.position.y,
            self.heading,
        )

        # Triple A for close range defense
        aa_group = self.add_auxiliary_group("AA")
        self.add_unit_to_group(
            aa_group,
            AirDefence.SPAAA_Vulcan_M163,
            "AAA",
            self.position + Point(20, 30),
            self.heading,
        )

        num_launchers = random.randint(3, 6)
        positions = self.get_circular_position(
            num_launchers, launcher_distance=120, coverage=180
        )

        for i, position in enumerate(positions):
            self.add_unit(
                AirDefence.SAM_Hawk_LN_M192,
                "LN#" + str(i),
                position[0],
                position[1],
                position[2],
            )

    @classmethod
    def range(cls) -> AirDefenseRange:
        return AirDefenseRange.Medium
