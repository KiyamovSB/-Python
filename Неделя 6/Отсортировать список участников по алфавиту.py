class Participant:
    name2 = ''
    name1 = ''
    school_number = 0
    point = 0

participants = []

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

lines = inFile.readlines()
for line in lines:
    tempParData = line.split()
    participant = Participant()
    participant.name2 = tempParData[0]
    participant.name1 = tempParData[1]
    participant.school_number = tempParData[2]
    participant.point = tempParData[3]
    participants.append(participant)

participants.sort(key=lambda p: p.name2)

for participant in participants:
    s = participant.name2+' '+participant.name1+' '+participant.point+'\n'
    outFile.write(s)

inFile.close()
outFile.close()
