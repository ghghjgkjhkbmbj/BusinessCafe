import os
os.environ["SDL_AUDIODRIVER"] = "directsound"

import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()

from Modules.Utility import *
from Modules.Scenes import *

screen = pygame.display.set_mode((512, 448))
pygame.display.set_caption("Business Hotline")

base_path = os.path.dirname(__file__)
IconPath = CreatePath(base_path, "Assets", "GameIcon.png")
GameIcon = pygame.image.load(IconPath).convert_alpha()
GameIcon = pygame.transform.scale(GameIcon, (150, 150))
pygame.display.set_icon(GameIcon)

SANS_SAAD = CreatePath(base_path, "Audio", "sans_saad.mp3")
PRESS_START = CreatePath(base_path, "Audio", "PressStartToPlay.mp3")
WRATH = CreatePath(base_path, "Audio", "THY_END_IS_NOW.mp3")

pygame.mixer.music.load(PRESS_START)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
running = True

FPS_LIMIT = 60
CURRENT_SCENE = "MAIN_MENU"
MENU_ACTIVE = False
FULLSCREENED = False

music_paused = False

DiaInit(pygame)
Init(pygame)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if IsKeyPressed(pygame, pygame.K_LCTRL):
                MENU_ACTIVE = not MENU_ACTIVE
            elif IsKeyPressed(pygame, pygame.K_z):
                if CURRENT_SCENE == "YOUR_ROOM":
                    ReturningData = YR_INTR(pygame, CURRENT_SCENE, screen)
                    CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
                elif CURRENT_SCENE == "Computer_Home":
                    ReturningData = CH_INTR(pygame, CURRENT_SCENE, screen)
                    CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
                elif CURRENT_SCENE == "NotYour_Room":
                    ReturningData = NYR_INTR(pygame, CURRENT_SCENE, screen)
                    CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
                elif CURRENT_SCENE == "COZY_CAFE":
                    ReturningData = CC_INTR(pygame, CURRENT_SCENE, screen)
                    CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
                elif CURRENT_SCENE == "CafeFull":
                    ReturningData = CF_INTR(pygame, CURRENT_SCENE, screen)
                    CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
                elif CURRENT_SCENE == "DAY_SELECT":
                    ReturningData = SD_INTR(pygame, CURRENT_SCENE, screen)
                    if ReturningData == 1:
                        CURRENT_SCENE = "YOUR_ROOM"
                        pygame.mixer.music.load(SANS_SAAD)
                        pygame.mixer.music.play(-1)
                elif CURRENT_SCENE == "MAIN_MENU":
                    CURRENT_SCENE = "DAY_SELECT"
                elif CURRENT_SCENE == "DAY1_COMP":
                    CURRENT_SCENE = "MAIN_MENU"
                    pygame.mixer.music.load(PRESS_START)
                    pygame.mixer.music.play(-1)
            elif IsKeyPressed(pygame, pygame.K_x):
                YR_CANCL(pygame)
            elif IsKeyPressed(pygame, pygame.K_UP):
                TEXT_OPTION_UP(pygame, CURRENT_SCENE)
            elif IsKeyPressed(pygame, pygame.K_DOWN):
                TEXT_OPTION_DOWN(pygame, CURRENT_SCENE)
            elif IsKeyPressed(pygame, pygame.K_TAB):
                FULLSCREENED = not FULLSCREENED

                if FULLSCREENED:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((512, 448))
            elif IsKeyPressed(pygame, pygame.K_0):
                music_paused = not music_paused

                if music_paused:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    pygame.mouse.set_visible(False)

    if CURRENT_SCENE == "YOUR_ROOM":
        pygame.display.set_caption("Business Cafe | Your Room")
        ReturningData = YourRoom_scene(pygame, screen, MENU_ACTIVE)
        CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
    elif CURRENT_SCENE == "Computer_Home":
        pygame.display.set_caption("Business Cafe | Computer")
        ReturningData = Computer_Home(pygame, screen, MENU_ACTIVE)
        CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
    elif CURRENT_SCENE == "NotYour_Room":
        pygame.display.set_caption("Business Cafe | Kitchen")
        ReturningData = NotYour_Room(pygame, screen)
        CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
    elif CURRENT_SCENE == "COZY_CAFE":
        pygame.display.set_caption("Business Cafe | Cozy Cafe")
        ReturningData = Cafe_Scene(pygame, screen)
        CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
    elif CURRENT_SCENE == "CafeFull":
        pygame.display.set_caption("Business Cafe | Cash Register")
        ReturningData = CafeFull_Scene(pygame, screen)
        CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
    elif CURRENT_SCENE == "MAIN_MENU":
        pygame.display.set_caption("Business Cafe | Main Menu")
        ReturningData = MainMenu_Scene(pygame, screen)
        CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
    elif CURRENT_SCENE == "DAY_SELECT":
        pygame.display.set_caption("Business Cafe | Time Machine That Allows You To Time Travel But Only Through a Poorly Made GUI.")
        ReturningData = DaySelect_Scene(pygame, screen)
        CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
    elif CURRENT_SCENE == "SECRET":
        pygame.mixer.music.pause()
        pygame.display.set_caption("Business Cafe | There is no escape.")
        ReturningData = SecretRoom(pygame, screen, MENU_ACTIVE)
        CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
    elif CURRENT_SCENE == "DAY1_COMP":
        pygame.mixer.music.pause()
        pygame.display.set_caption("Business Cafe | You did it!")
        ReturningData = Day1_COMP_Scene(pygame, screen)
        CURRENT_SCENE = ProcessReturnedData(ReturningData, CURRENT_SCENE)
    else:
        screen.fill("black")

    pygame.display.flip()

    clock.tick(FPS_LIMIT)

pygame.quit()

