#!/usr/bin/env python3
from time import sleep
from typing import List

import chess

from ai import aiController
from speech import SpeechInput
from game import Game
from motionPlanner import MotionPlanner
from controller import Controller
from game import Game

from datatypes import *


def main():
    speech = SpeechInput()
    ai = aiController()
    planner = MotionPlanner()
    controller = Controller()

    game = Game()

    while True:
        if game.board.turn == chess.WHITE:
            print(game.board)
            command = speech.getCommand()
            aiMove = False
        else:
            command = ai.getMove(game.board)
            aiMove = True

        if command == 'show':
            print(game.board)
        elif command:
            implementation = game.implementMove(str(command))

            if aiMove and not implementation:
                print(game.board)
                raise Exception("The AI tried to make the move {}, which is apparently illegal.".format(command))

            for m in implementation:
                steps = planner.make_command_list(m)  # type:List[Action]

                for step in steps:
                    controller.makeMove(step)

        else:
            sleep(0.01)


if __name__ == '__main__':
    main()
