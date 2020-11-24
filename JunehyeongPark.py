
class JunehyeongPark:
    student_Name = ""
    student_Hand = []
    # student function uses student Hand and return a boolean list to exchange cards
    def student_function(self):
        import itertools
        import random
        from deuces import Card
        from deuces import Evaluator

        def CreateDeckStudent(cards):
            deck = []
            DBShortCardNames = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
            DBShortSuitNames = ['c', 'd', 'h', 's']

            for c in itertools.product(DBShortCardNames, DBShortSuitNames):
                crd = c[0] + c[1]
                DummyCreate = 0
                for ii in cards:
                    if crd == ii:
                        DummyCreate = DummyCreate + 1
                if DummyCreate == 0:
                    deck.append(crd)
            random.shuffle(deck)
            return deck

        def CheckFn(cards):
            newhand = []
            for i in range(0, 5):
                newhand.append(Card.new(cards[i]))
            point = eval.evaluate(board, newhand)
            return point

        base=self.student_Hand
        b1 = base[0]
        b2 = base[1]
        b3 = base[2]
        b4 = base[3]
        b5 = base[4]
        print(base)
        eval = Evaluator()
        board = []
        Sampling = 1000 # Number of samples

        Possible0 = CheckFn(base)

        Possible1 = 20000
        P1_position = 0
        for i1 in range(0,5):
            Point_dummy = 0
            Point_dummy_i = 0
            Dummy_base = [b1, b2, b3, b4, b5]
            for ki in range(0,Sampling):
                deck1 = CreateDeckStudent([b1, b2, b3, b4, b5])
                Dummy_base[i1] = deck1[0]
                Point_dummy_i = Point_dummy_i + 1
                Point_dummy = Point_dummy + CheckFn(Dummy_base)
            if (Point_dummy / Point_dummy_i) < Possible1:
                Possible1 = Point_dummy / Point_dummy_i
                P1_position = i1

        Possible2 = 20000
        P2_position = [0,0]
        P2_position_list = [[0,1], [0,2], [0,3], [0,4],
                            [1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
        for i2 in P2_position_list:
            Point_dummy = 0
            Point_dummy_i = 0
            Dummy_base = [b1, b2, b3, b4, b5]
            for ki in range(0,Sampling):
                deck1 = CreateDeckStudent([b1, b2, b3, b4, b5])
                Dummy_base[i2[0]] = deck1[0]
                Dummy_base[i2[1]] = deck1[1]
                Point_dummy_i = Point_dummy_i + 1
                Point_dummy = Point_dummy + CheckFn(Dummy_base)
            if (Point_dummy / Point_dummy_i) < Possible2:
                Possible2 = Point_dummy / Point_dummy_i
                P2_position = i2

        Possible3 = 20000
        P3_position = [0, 0, 0]
        P3_position_list = [[0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 2, 3], [0, 2, 4], [0, 3, 4],
                            [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
        for i3 in P3_position_list:
            Point_dummy = 0
            Point_dummy_i = 0
            Dummy_base = [b1, b2, b3, b4, b5]
            for ki in range(0,Sampling):
                deck1 = CreateDeckStudent([b1, b2, b3, b4, b5])
                Dummy_base[i3[0]] = deck1[0]
                Dummy_base[i3[1]] = deck1[1]
                Dummy_base[i3[2]] = deck1[2]
                Point_dummy_i = Point_dummy_i + 1
                Point_dummy = Point_dummy + CheckFn(Dummy_base)
            if (Point_dummy / Point_dummy_i) < Possible3:
                Possible3 = Point_dummy / Point_dummy_i
                P3_position = i3

        Possible4 = 20000
        P4_position = [0, 0, 0, 0]
        P4_position_list = [[0, 1, 2, 3], [0, 1, 2, 4], [0, 1, 3, 4],
                            [0, 2, 3, 4], [1, 2, 3, 4]]
        for i4 in P4_position_list:
            Point_dummy = 0
            Point_dummy_i = 0
            Dummy_base = [b1, b2, b3, b4, b5]
            for ki in range(0,Sampling):
                deck1 = CreateDeckStudent([b1, b2, b3, b4, b5])
                Dummy_base[i4[0]] = deck1[0]
                Dummy_base[i4[1]] = deck1[1]
                Dummy_base[i4[2]] = deck1[2]
                Dummy_base[i4[3]] = deck1[3]
                Point_dummy_i = Point_dummy_i + 1
                Point_dummy = Point_dummy + CheckFn(Dummy_base)
            if (Point_dummy / Point_dummy_i) < Possible4:
                Possible4 = Point_dummy / Point_dummy_i
                P4_position = i4

        Point_dummy = 0
        Point_dummy_i = 0
        Dummy_base = [b1, b2, b3, b4, b5]
        for ki in range(0, Sampling):
            deck1 = CreateDeckStudent([b1, b2, b3, b4, b5])
            Dummy_base = deck1[0:5]
            Point_dummy_i = Point_dummy_i + 1
            Point_dummy = Point_dummy + CheckFn(Dummy_base)
        Possible5 = Point_dummy / Point_dummy_i

        Possible_all = [Possible0, Possible1, Possible2, Possible3, Possible4, Possible5]
        answer = [False, False, False, False, False]

        if min(Possible_all) == Possible1:
            answer[P1_position] = True
        elif min(Possible_all) == Possible2:
            answer[P2_position[0]] = True
            answer[P2_position[1]] = True
        elif min(Possible_all) == Possible3:
            answer[P3_position[0]] = True
            answer[P3_position[1]] = True
            answer[P3_position[2]] = True
        elif min(Possible_all) == Possible4:
            answer[P4_position[0]] = True
            answer[P4_position[1]] = True
            answer[P4_position[2]] = True
            answer[P4_position[3]] = True
        elif min(Possible_all) == Possible5:
            answer = [True, True, True, True, True]
        print(answer)

        #return [False, False, False, False, True]
        return answer
