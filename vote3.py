#total seats in current election(change to read in.. get from genesis block)
total_seats = 158
#list of candidates to be read into program from system.
candidates = {}
#Read candidates from file
canditate_list = open('./info/candidates.txt', 'r')
#Read in every candidate from file and add to dictionary added above, key = name, value = vote count  (0)
for candidate in canditate_list:
    candidate = candidate.strip()
    #store in tuple, used to add in dictionary
    (key, val) = candidate.split(',')
    candidates[key] = val
canditate_list.close()
print(candidates)


def verify():
    ''' Voter verification method.
        Text file serves as voter register
        Deny any not in file'''
    # Read in list of voters to application for verification
    voters = []
    voter_list = open('./info/voters.txt', 'r')
    for voter in voter_list:
        #strip leading and trailing characters, does not work without
        voter = voter.strip()
        #add the voter from file to list
        voters.append(voter)
    voter_list.close
    voter_id = input('enter your voter ID: ')
    if voter_id in voters:
        #Print for testing, authenticated
        print('valid')
        # Allow to vote
        vote()
    else:
        if verify.counter >= 3:
                print('Too many attempts')
                print('!!!!Method needed to lock system!!!!')
                return False 
        else:
            #Not found
            print('invalid') 
            #Increment counter to count attempts
            verify.counter = verify.counter +  1
            print('count' + str(verify.counter))
            #Recall method so the counter does not go back to 0 - without this it will exit function and then recall it leading count to go to 0
            verify()

        
def vote():
    ''' Allows user to vote for candidate, this increments each vote count by one then updates record on file.'''
    cast_vote = input('Vote for candidate: \n1. Tom \n2. Jessica \n3. Derek \n4. Samantha\n5. Albert \nCandidate You wish to Vote for: ')
    if cast_vote == '1':
        candidates['tom'] = int(candidates['tom']) + 1
        print('total votes ' + str(candidates['tom']))
        print('voted for Tom')

        
    elif cast_vote == '2':
        candidates['jessica'] = int(candidates['jessica']) + 1
        print('total votes ' + str(candidates['jessica']))
        print('voted for jessica')


    elif cast_vote == '3':
        candidates['derek'] = int(candidates['derek']) + 1
        print('total votes ' + str(candidates['derek']))
        print('voted for derek')
        

    elif cast_vote == '4':
        candidates['samantha'] = int(candidates['samantha']) + 1
        print('total votes ' + str(candidates['samantha']))
        print('voted for samantha')
        

    elif cast_vote == '5':
        candidates['albert'] = int(candidates['albert']) + 1
        print('total votes ' + str(candidates['albert']))
        print('voted for albert')
        
    else:
        print('Invalid option!')
    update()
    
    

#def prstv(total_seats, candidates, votecount, candidate_total):



def update():
    ''' Update the file on system for total votes 
        Got from dictionary, runs @ vote()'''
    key = ''
    value = ''
    total_votes = 0
    cfile =  open('./info/candidates.txt', 'w')
    for candidate in candidates:
        key = candidate
        value = candidates[key]
        total_votes = total_votes + int(value)
        print(key, value)
        cfile.write(key + ',' + str(value) + '\n')
    print('total votes: ', str(total_votes))

def view():
    ''' Print out the current votes on disk'''
    for candidate in candidates:
        print('Candidate: ' + str(candidate) + ' -- Vote count: ' + str(candidates[candidate]))


while True:
    #counter to track no. of attmepted auths. defined outside of function as inside would reset.
    verify.counter = 0
    usrinput = input('1. Vote \n2. View candidates \n3. Tally \n>>')
    print(candidates) 
    if usrinput == '1':
        verify()
    elif usrinput == '2':
        view()
    elif usrinput == '3':
        prstv(total_seats, candidates, total_votes )
    else:
        print('Invalid option')