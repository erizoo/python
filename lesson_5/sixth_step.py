subj = {}


def getHoursLessonsFromString(val):
    if val != '-':
        return val.split("(")[0]
    else:
        return "0"


with open('sixth_step_file.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(getHoursLessonsFromString(lecture)) + int(getHoursLessonsFromString(practice)) + int(
            getHoursLessonsFromString(lab))
    print(f'Общее количество часов по предмету - \n {subj}')
