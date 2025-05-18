from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class MarvelRivalsArchipelagoOptions:
    pass


class MarvelRivalsGame(Game):
    name = "Marvel Rivals"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = MarvelRivalsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Perform at least 1 of the following Team-Up Abilities: ABILITIES",
                data={
                    "ABILITIES": (self.team_up_abilities, 3),
                },
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Win a match as HERO",
                data={
                    "HERO": (self.heroes, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=9,
            ),
            GameObjectiveTemplate(
                label="Win a Domination match on MAP",
                data={
                    "MAP": (self.maps_domination, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a Convoy match on MAP",
                data={
                    "MAP": (self.maps_convoy, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a Convergence match on MAP",
                data={
                    "MAP": (self.maps_convergence, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a Conquest match on MAP",
                data={
                    "MAP": (self.maps_conquest, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a Doom Match on MAP",
                data={
                    "MAP": (self.maps_doom_match, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win COUNT GAME_MODE matches",
                data={
                    "COUNT": (self.game_mode_count_range, 1),
                    "GAME_MODE": (self.game_modes, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get a K.O. streak of at least COUNT as HERO",
                data={
                    "COUNT": (self.kill_streak_count_range, 1),
                    "HERO": (self.heroes, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
        ]

    @staticmethod
    def team_up_abilities() -> List[str]:
        return [
            "Allied Agents",
            "Ammo Overload",
            "Arcane Order",
            "Atlas Bond",
            "Chilling Charisma",
            "Dimensional Shortcut",
            "ESU Alumnus",
            "Fantastic Four",
            "Fastball Special",
            "Gamma Charge",
            "Guardian Revival",
            "Lunar Force",
            "Mental Projection",
            "Planet X Pals",
            "Ragnarok Rebirth",
            "Stars Aligned",
            "Storming Ignition",
            "Symbiote Bond",
        ]

    @staticmethod
    def maps_domination() -> List[str]:
        return [
            "Hellfire Gala: Krakoa",
            "Hydra Charteris Base: Hell's Heaven",
            "Intergalactic Empire of Wakanda: Birnin T'Challa",
            "Yggsgard: Royal Palace",
        ]

    @staticmethod
    def maps_convoy() -> List[str]:
        return [
            "Empire of Eternal Night: Midtown",
            "Tokyo 2099: Spider-Islands",
            "Yggsgard: Yggdrasill Path",
        ]

    @staticmethod
    def maps_convergence() -> List[str]:
        return [
            "Intergalactic Empire of Wakanda: Hall of Djalia",
            "Klyntar: Symbiotic Surface",
            "Tokyo 2099: Shin-Shibuya",
            "Empire of Eternal Night: Central Park",
        ]

    @staticmethod
    def maps_conquest() -> List[str]:
        return [
            "Tokyo 2099: Warped Ninomaru",
        ]

    @staticmethod
    def maps_doom_match() -> List[str]:
        return [
            "Empire of Eternal Night: Sanctum Sanctorum",
        ]

    @staticmethod
    def heroes() -> List[str]:
        return [
            "Adam Warlock",
            "Black Panther",
            "Black Widow",
            "Captain America",
            "Cloak & Dagger",
            "Doctor Strange",
            "Emma Frost",
            "Groot",
            "Hawkeye",
            "Hela",
            "Hulk",
            "Human Torch",
            "Invisible Woman",
            "Iron Fist",
            "Iron Man",
            "Jeff the Land Shark",
            "Loki",
            "Luna Snow",
            "Magik",
            "Magneto",
            "Mantis",
            "Mister Fantastic",
            "Moon Knight",
            "Namor",
            "Peni Parker",
            "Psylocke",
            "Rocket Raccoon",
            "Scarlet Witch",
            "Spider-Man",
            "Squirrel Girl",
            "Star-Lord",
            "Storm",
            "The Punisher",
            "The Thing",
            "Thor",
            "Venom",
            "Winter Soldier",
            "Wolverine",
        ]

    @staticmethod
    def game_mode_count_range() -> range:
        return range(2, 6)

    @staticmethod
    def game_modes() -> List[str]:
        return [
            "Convergence",
            "Convoy",
            "Domination",
        ]

    @staticmethod
    def kill_streak_count_range() -> range:
        return range(3, 9)


# Archipelago Options
# ...
