from art import logo, vs
from game_data import data
import random
import clear

def get_random_element():
  return data[random.randint(0, len(data)-1)]

def compare(first_count, second_count, who):
  correct_answer = False
  if first_count > second_count and who == 'A':
    correct_answer = True
  elif second_count > first_count and who == 'B':
    correct_answer = True
  return correct_answer

def print_compare_messages(first_element, second_element):
  print(f"Compare A: {first_element['name']}, a {first_element['description']}, from {first_element['country']}")
  print(vs)
  print(f"Against B: {second_element['name']}, a {second_element['description']}, from {second_element['country']}")

def start_game():
  score = 0
  game_over = False
  first_element = get_random_element()
  second_element = get_random_element()
  if(first_element == second_element):
    second_element = get_random_element()
  
  while not game_over:
    print(logo)
    print_compare_messages(first_element, second_element)
    selection = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear.clear()
    print(logo)
    correct_answer = compare(first_element['follower_count'], second_element['follower_count'], selection)
    if correct_answer:
      first_element = second_element
      second_element = get_random_element()
      score += 1
      print(f"You are right! Current score: {score}")
    else:
      game_over = True
      print(f"Sorry, that's wrong. Final score: {score}")
  

start_game()