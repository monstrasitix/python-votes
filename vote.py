from os import system, name 
  

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 


#-----------------------------------
#   Utilities
#-----------------------------------


def strip(value):
    return value.strip()



def populate_file(reader, callback):
    for line in reader:
        callback(map(strip, line.split(',')))
    reader.close()


#-----------------------------------
#   Constant paths
#-----------------------------------


PATH_VOTERS = './info/voters.txt'
PATH_CANDIDATE = './info/candidates.txt'


#-----------------------------------
#   Global memory
#-----------------------------------


voters = []
candidates = {}
loop = True


#-----------------------------------
#   Entity parsing
#-----------------------------------


def parse_candidate((name, vote_count)):
    candidates[name] = int(vote_count)

def read_candidates():
    populate_file(open(PATH_CANDIDATE, 'r'), parse_candidate)


def parse_voter(vote):
    voters.append(int(vote[0]))

def read_voters():
    populate_file(open(PATH_VOTERS, 'r'), parse_voter)



#-----------------------------------
#   Actions
#-----------------------------------


def voter_exists(voter_id):
    return voter_id in voters


def candidate_list():
    candidate_string = ''

    for index, candidate in enumerate(candidates, start=1):
        candidate_string += '\n{}. {}'.format(index, candidate)

    return candidate_string


def vote();
    voter_input = input('Vote for candidate: ' + candidate_list() + '\n>> ')
    # Not sure what to do

def action_vote():
    read_voters()
    read_candidates()

    voter_input = input('Enter your voter ID: ')

    if voter_exists(voter_input.strip()):
        vote()
    else:
        print('action_vote no')


def action_view_candidates():
    for name in candidates:
        print(
            'Candidate: {} -- Vote count: {}'.format(name, candidates[name])
        )


def action_tally():
    print('action_tally')


def action_exit():
    global loop
    loop = False


#-----------------------------------
#   Initialization
#-----------------------------------


def proceed():
    raw_input('\nPress Enter to continue...\n')
    clear()


clear()


cli_options = {
    1: ('Vote', action_vote),
    2: ('View candidates', action_view_candidates),
    3: ('Tally', action_tally),
    4: ('Exit', action_exit),
}

def get_options():
    output = ''

    for index in cli_options:
        (name, action) = cli_options[index]
        output += '\n{} {}'.format(index, name)

    return output


read_voters()
read_candidates()


while loop:
    user_input = input('{}\n>> '.format(get_options()))
    clear()

    if user_input in cli_options:
        (name, action) = cli_options[user_input]
        action()
    else:
        print('Invalid option')

    proceed()

    