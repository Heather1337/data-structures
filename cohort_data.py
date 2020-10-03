"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    #first_name|last_name|house|adviser|cohort_name
    houses = set()

    house_open_file = open(filename)
    for line in house_open_file:
      words = line.split("|")
      house = words[2]
      if house != "":
        houses.add(house)
    
    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """


    students = []

    student_file = open(filename)
    for line in student_file:
      line = line.rstrip()
      words = line.split("|") #[Harry, Potter, Gryffindor, McGonagall, Fall 2015]
      student_name = str(words[0])+ " " + str(words[1])
      student_cohort = words[4]

      #Check for cases if cohort is ALL
      if cohort == "All":
        if student_cohort != "G" and student_cohort != "I":
          students.append(student_name)
      #Check for cases if cohort is provided
      elif cohort == student_cohort:
        students.append(student_name)   

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []
 
    school_file = open(filename)
    for line in school_file:
      line = line.rstrip()
      words = line.split('|') 
      student_name = str(words[0])+ " " + str(words[1])
      student_house = words[2]
      student_cohort = words[4]

      if student_house == "Gryffindor":
        gryffindor.append(student_name)
      if student_house == "Ravenclaw":
        ravenclaw.append(student_name)
      if student_house == "Hufflepuff":
        hufflepuff.append(student_name)
      if student_house == "Slytherin":
        slytherin.append(student_name)
      if student_house == "Dumbledore's Army":
        dumbledores_army.append(student_name)
      if student_cohort == "I":
        instructors.append(student_name)
      if student_cohort == "G":
        ghosts.append(student_name)

    dumbledores_army.sort()
    gryffindor.sort()
    hufflepuff.sort()
    ravenclaw.sort()
    slytherin.sort()
    ghosts.sort()
    instructors.sort()
    return [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    school_file = open(filename)
    for line in school_file:
      line = line.rstrip()
      words = line.split('|')
      first_name, last_name, house, adviser, cohort = words
      student_tuple = (first_name + ' ' + last_name, house, adviser, cohort)

      all_data.append(student_tuple)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    school_file = open(filename)
    for line in school_file:
      line = line.rstrip()
      words = line.split('|')
      first_name, last_name, house, adviser, cohort = words

      if (first_name + ' ' + last_name) == name:
        if cohort == '':
          return 
        else:
           return cohort


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    unique_names_set = set()
    names = []
    #check name and if doesn't exist in list then add to list
    #if it does exist in the list then add to dupes list


    school_file = open(filename)
    for line in school_file:
      line = line.rstrip()
      words = line.split('|')
      last_name = words[1]
      if last_name in names:
        unique_names_set.add(last_name)
      else:
        names.append(last_name)

    return unique_names_set






def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    housemates = set()
    given_student_house = ''
    given_student_cohort = ''
 
    school_file = open(filename)
    for line in school_file:
      line = line.rstrip()
      words = line.split('|')
      first_name, last_name, house, adviser, cohort = words
      if first_name + ' ' + last_name == name:
        given_student_house = house 
        given_student_cohort = cohort

    school_file_open = open(filename)
    for line in school_file_open:
      line = line.rstrip()
      words = line.split('|')
      first_name, last_name, house, adviser, cohort = words

      if house == given_student_house and cohort == given_student_cohort and name != first_name + ' ' + last_name:
        housemates.add(first_name + ' ' + last_name) 
    
    return housemates
      
    



##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
