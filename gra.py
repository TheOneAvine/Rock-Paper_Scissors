import pygame, os, time, pip
from sys import exit
from random import *

pip.main(["install", "pygame"])

#this makes life easier
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#here starts pygame
pygame.init() 
clock = pygame.time.Clock()

#win counts 
player_wins_count = 0
comp_wins_count = 0
tie = 0

#all pics needed and their rectangles
table_png = pygame.image.load("graphics/table.png")
comp_rock = pygame.image.load("graphics/hand comp rock.png")
comp_paper = pygame.image.load("graphics/hand comp paper.png")
comp_scissors = pygame.image.load("graphics/hand comp scissors.png")
player_rock = pygame.image.load("graphics/hand player rock.png")
player_rock_rect = player_rock.get_rect(center = (260, 500))
player_paper = pygame.image.load("graphics/hand player paper.png")
player_paper_rect = player_paper.get_rect(center = (400, 500))
player_scissors = pygame.image.load("graphics/hand player scissors.png")
player_scissors_rect = player_scissors.get_rect(center = (540, 500))

#lists of possible computer choices
comp_choose_list = [comp_rock, comp_paper, comp_scissors]

#function for checking who won
def who_wins():
    random_number = randrange(0,3)
    main_window.blit(comp_choose_list[random_number], (377, 130))
    
    #possible player wins
    if random_number == 0 and player_choice_num == 0 or random_number == 2 and player_choice_num == 1 or random_number == 1 and player_choice_num == 2:
        main_window.blit(in_action_player_wins_surface, player_wins_rect)
        global player_wins_count
        player_wins_count += 1

    #possible computer wins
    elif random_number == 1 and player_choice_num == 1 or random_number == 0 and player_choice_num == 2 or random_number == 2 and player_choice_num == 0:
        main_window.blit(in_action_comp_wins_surface, comp_rect)
        global comp_wins_count
        comp_wins_count += 1
    
    #tie
    else:
        main_window.blit(in_action_tie_surface, tie_rect)
        global tie
        tie += 1
    pygame.display.flip()

    #this has to exist so that the player can actually see the result
    pygame.time.delay(1200)   

#now we game
while True:
    #obviously we need to be able to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #that is where we play, stays constant
    main_window = pygame.display.set_mode((800, 600)) 
    pygame.display.set_caption("Rock, Paper, Scissors")
    main_window.fill('white')
    main_window.blit(table_png, (120,90))


    #that is needed to display counts from above
    player_wins_font = pygame.font.Font('graphics/pixel.ttf', 30)
    player_wins_surface = player_wins_font.render("Player wins: "+str(player_wins_count), False, 'black')
    comp_wins_font = pygame.font.Font('graphics/pixel.ttf', 30)
    comp_wins_surface = comp_wins_font.render("Computer wins: "+str(comp_wins_count), False, 'black')
    tie_font = pygame.font.Font('graphics/pixel.ttf', 30)
    tie_surface = tie_font.render("Tie: "+str(tie), False, 'black')

    #this is needed to announce who won
    in_action_tie_font = pygame.font.Font('graphics/pixel.ttf', 50)
    in_action_tie_surface = tie_font.render("Tie!", False, 'black')
    tie_rect = in_action_tie_surface.get_rect(center = (400, 240))
    in_action_player_wins_font = pygame.font.Font('graphics/pixel.ttf', 50)
    in_action_player_wins_surface = player_wins_font.render("Player wins!", False, 'black')
    player_wins_rect = in_action_player_wins_surface.get_rect(center = (400, 240))
    in_action_comp_wins_font = pygame.font.Font('graphics/pixel.ttf', 50)
    in_action_comp_wins_surface = comp_wins_font.render("Computer wins!", False, 'black')
    comp_rect = in_action_comp_wins_surface.get_rect(center = (400, 240))

    #here are displayed counts
    main_window.blit(player_wins_surface, (10,10))
    main_window.blit(comp_wins_surface, (300,10))
    main_window.blit(tie_surface, (650,10))

    #sprites available for the player
    rock = main_window.blit(player_rock, player_rock_rect)
    paper = main_window.blit(player_paper, player_paper_rect)
    scissors = main_window.blit(player_scissors, player_scissors_rect)

    #actually we game now
    if event.type == pygame.MOUSEBUTTONDOWN:
        if paper.collidepoint(event.pos):
            player_choice_num = 0
            main_window.blit(player_paper, (370, 270))

            who_wins()

        if rock.collidepoint(event.pos):
            player_choice_num = 1
            main_window.blit(player_rock, (370, 270))
            who_wins()
            
        if scissors.collidepoint(event.pos):
            player_choice_num = 2
            main_window.blit(player_scissors, (370, 270))
            who_wins()
            print(tie, player_wins_count, comp_wins_count)
         
    
    pygame.display.flip()
    #max fps
    clock.tick(30)



