'''

Rules of the game:

Two decks of cards between -10 and 10.  Player is presented 2 cards at random (shuffle-mix both decks).

Goal is to stay within 21 for 31 cards (with a final card to force the ending.).

Imagine two 'towers' of cards 15 each.  You can continuously draw on either side, but the goal is to reach the 31st card.

'''

import random
import os
import PySimpleGUI as sg
print(os.getcwd())

CARDS_DIR = os.path.join(os.getcwd(),'Cards')
print(CARDS_DIR)


CARDS_PER_SIDE = 15


INSTRUCTIONS = '''
Welcome to Zero 21 Solitaire!  

        Select a card (1 or 2) to play it.
        Place one of those cards on reserve (q or w).
        To play a reserve card, press 'r'.  You may not reserve more than one card.
        You may not discard a reserve card.  You must play it.
'''

def generate_deck(number_of_stacks = 4):
    return [i for i in range(-10,11)] * number_of_stacks

def set_up_cards(deck):
    all_cards_in_game = random.sample(deck, k=32)
    left_side = all_cards_in_game[0:CARDS_PER_SIDE + 1] # 0:16
    right_side = all_cards_in_game[CARDS_PER_SIDE + 1:31] # 16:31
    last_card = all_cards_in_game[31] # 31
    
    return left_side, right_side, last_card


def main(INSTRUCTIONS):


    deck = generate_deck()

    left_side, right_side = [-1], [-1]

    while left_side[0] < 0 and right_side[0] < 0:
        left_side, right_side, last_card = set_up_cards(deck)
    


    running_total = 0

    you_lose = False

    reserve_card = ''

    sg.change_look_and_feel('lightgrey')

    layout = [
        [sg.Multiline(INSTRUCTIONS, text_color='darkblue', background_color='antiquewhite',)],
        [sg.Text(' '*100, key='LastCard')],
        [sg.Text(f'Running Total: {running_total}', key='Running Total')],
        [sg.Text(f'{left_side[0]}   {right_side[0]}                           ', key='Cards')],
        [sg.Text(f'Reserve Card: {reserve_card}                               ', key='Reserve')],
        [sg.Button('Left', image_filename=CARDS_DIR + "/" +str(left_side[0]) + '.png',key='Left'), sg.Button('Right', image_filename=CARDS_DIR + "/" + str(right_side[0]) + '.png')],
        [sg.Button('Store Left'), sg.Button('Store Right')],
        [sg.Button('Use Reserve')],
        [sg.ProgressBar(orientation='v',size=(20, 20), key='num_left', max_value=CARDS_PER_SIDE), sg.ProgressBar(orientation='v',size=(20, 20), key='num_right', max_value=CARDS_PER_SIDE)],
        [sg.Button('New Game')],
    ]

    # Create the Window
    window = sg.Window('Solitaire', layout)


    def update_cards():
        if len(left_side) > 0 and len(right_side) > 0:
            window['num_left'].UpdateBar(len(left_side))
            window['num_right'].UpdateBar(len(right_side))
            window['Cards'].update(f'{left_side[0]} {right_side[0]}')
            window.Element('Left').Update(image_filename=CARDS_DIR + "/" +str(left_side[0]) + '.png')
            window.Element('Right').Update(image_filename=CARDS_DIR + "/" + str(right_side[0]) + '.png', image_size=(10,10))

        elif len(left_side) == 0 and len(right_side) == 0:
            window['Cards'].update(f'(Use Last Card) (Use Last Card)')
            window['LastCard'].update(f'Last Card: {last_card}')
            window['num_left'].UpdateBar(len(left_side))
            window['num_right'].UpdateBar(len(right_side))
            window.Element('Left').Update(image_filename=CARDS_DIR + "/last.png")
            window.Element('Right').Update(image_filename=CARDS_DIR + "/last.png")


        elif len(right_side) == 0 and len(left_side) > 0:
            window['Cards'].update(f'{left_side[0]} (Use Last Card)')
            window['LastCard'].update(f'Last Card: {last_card}')
            window['num_left'].UpdateBar(len(left_side))
            window['num_right'].UpdateBar(len(right_side))
            window.Element('Left').Update(image_filename=CARDS_DIR + "/" + str(left_side[0]) + '.png')
            window.Element('Right').Update(image_filename=CARDS_DIR + "/last.png")

        elif len(left_side) == 0 and len(right_side) > 0:
            window['Cards'].update(f'(Use Last Card) {right_side[0]}')
            window['LastCard'].update(f'Last Card: {last_card}')
            window['num_left'].UpdateBar(len(left_side))
            window['num_right'].UpdateBar(len(right_side))
            window.Element('Left').Update(image_filename=CARDS_DIR + "/last.png")
            window.Element('Right').Update(image_filename=CARDS_DIR + "/" + str(right_side[0]) + '.png')


        window['Running Total'].update(f'Running total: {running_total}')
        if running_total >= 0 and running_total <= 21 and last_card =='':
            window['Reserve'].update("You WON!  Click New Game.")
        else:
            window['Reserve'].update(f'reserve card: {reserve_card}')

        if running_total < 0 or running_total > 21:
            window['Reserve'].update(f'You lost.  Lost lost lost.')


    #update_cards()
    running = True

    while running:

        event, values = window.read()

        update_cards()

        final_card_in_play = len(left_side) == 0 or len(right_side) == 0

        if event == 'Left':
            try:
                running_total += left_side[0]
                left_side.pop(0)
                update_cards()
            except:
                pass
        elif event == 'Right':
            try:
                running_total += right_side[0]
                right_side.pop(0)
                update_cards()
            except:
                pass
        elif event == 'Use Reserve':
            if reserve_card == '':
                window['Reserve'].update('You have nothing on reserve.')
            else:
                running_total += reserve_card
                reserve_card = ''
                window['Reserve'].update(f'reserve card: {reserve_card}')
                update_cards()

        elif event in ('Store Left',  'Store Right'):

            if reserve_card != '':
                print('You already have something on reserve.')
                pass
            else:
                if event == 'Store Left':
                    try:
                        reserve_card = left_side[0]
                        window['Reserve'].update(f'reserve_card: {reserve_card}')
                        left_side.pop(0)
                        update_cards()
                    except:
                        pass
                elif event == 'Store Right':
                    try:
                        reserve_card = right_side[0]
                        window['Reserve'].update(f'reserve card: {reserve_card}')
                        right_side.pop(0)
                        update_cards()
                    except:
                        pass

        elif event in ('New Game'):
            window.close()
            main(INSTRUCTIONS='')

        you_lose = (running_total >= 21) or (running_total < 0)

        if you_lose:
            while running:
                event, values = window.read()
                window['Reserve'].update('You lost.  Click New Game.')
                if event not in ('New Game'):
                    pass

                else:
                    window.close()
                    main(INSTRUCTIONS='')

        if final_card_in_play:
            if last_card == '':
                while running:
                    event, values = window.read()
                    window['Reserve'].update("You WON!  Click New Game.")
                    if event not in ('New Game'):
                        pass

                    else:
                        window.close()
                        main(INSTRUCTIONS='')

            elif len(left_side) == 0:
                if event == 'Left':
                    running_total += last_card
                    last_card = ''
                    update_cards()
                    if running_total >= 0 and running_total <= 21:
                        window['Reserve'].update("You WON!  Click New Game.")

            elif len(right_side)== 0:
                if event == 'Right':
                    running_total += last_card
                    last_card = ''
                    update_cards()
                    if running_total >= 0 and running_total <= 21:
                        window['Reserve'].update("You WON!  Click New Game.")



if __name__ == '__main__':
    main(INSTRUCTIONS)