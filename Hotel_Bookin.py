from datetime import date


class hotel:
    def __init__(self):
        self.rooms = {}
        self.available_rooms = {'std': [103, 104, 105],'delux': [203, 204, 205],'execu': [407, 408, 409], 'suit': [600, 601, 602],}
        self.roomprice = {1:2000, 2:4000, 3:5000, 4:6000}
    def check_in(self, name, address, phone):
        roomtype = int(input('Room types:\n1. standard \n2. deluxe \n3. Executive \n4. suite\n select a room type: '))
        if roomtype==1:
            if self.available_rooms['std']:
                room_no = self.available_rooms['std'].pop()
            else:
                print('sorry,standard room not available')
                return
        elif roomtype==2:
            if self.available_rooms['delux']:
                room_no = self.available_rooms['delux'].pop()
            else:
                print('sorry,deluxe room not available')
                return
        elif roomtype==3:
            if self.available_rooms['execu']:
                room_no = self.available_rooms['execu'].pop()
            else:
                print('sorry,executive room not available')
                return
        elif roomtype==4:
            if self.available_rooms['suit']:
                room_no = self.available_rooms['suit'].pop()
            else:
                print('sorry,suite room not available')
                return
        else:
            print('choose a valid room type')
        d, m, y=map (int, input('Enter check-in-date- in date,month,year').split())
        check_in = date (y, m, d)
        self.rooms[room_no] = {
            'name' : name,
            'address' : address,
            'phone' : phone,
            'check_in_date' : check_in,
            'room_type' : roomtype,
            'roomsevice' : 0
        }
        print(f"checked in {name}, {address}, to room: {room_no} on {check_in}")
    def room_service(self, room_no):
        c = int(input("select your choice: "))
        if room_no in self.rooms:
            print("***Hotel Menu***")
            print("1.Break fast:Rs.20 2. lunch:Rs.70 3.Dinner:Rs.120 4. Exit")
            while  1:
                if c == 1:
                    q = int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice'] += 20*q
                elif c == 3:
                    q = int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice'] += 70*q
                elif c == 3:
                    q = int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice'] += 120*q
                elif c == 4:
                    break
                else:
                    print("Invalid option")
                    print("room service Rs:", self.rooms[room_no]['roomservice'], "\n")
        else:
            print('Invalid room number')

    def display_occupied(self):
        if not self.rooms:
            print("not rooms are occupied at the moment. ")
        else:
            print("Occupied Rooms: ")
            print("__________________")
            print('room no. Name Phone')
            print("_____________________")
            for room_number, details in self.rooms.items():
                print(room_number, '\t', details['name'],'\t',details['phone'])

    def check_out(self, room_number):
        if room_number in self.rooms:
            check_out_date  = date.today()
            check_in_date = self.rooms[room_number]['check_in_date']
            duration = (check_out_date-check_in_date).days
            roomtype=self.rooms[room_number]['room_type']
            if roomtype == 1:
                self.available_rooms['std'].append(room_number)
            elif roomtype == 2:
                self.available_rooms['delux'].append(room_number)
            elif roomtype == 3:
                self.available_rooms['execu'].append(room_number)
            elif roomtype == 3:
                self.available_rooms['suit'].append(room_number)
            print('---------------------------')
            print(' Hotel Reciept')
            print(f"Name:{self.rooms[room_number]['name']}\nAddress:{self.rooms[room_number]['address']}")
            print(f"Phone:{self.rooms[room_number]['phone']}")
            print(f"Room Number:{room_number}")
            print(f"Check in date:{check_in_date.strftime('%d, %B, %Y')}")
            print(f"Check out date:{check_out_date.strftime('%d, %B, %Y')}")
            print(f"No.of Days: {duration}\tPrice per day:Rs.{self.roomprice[roomtype]}")
            roombill = self.roomprice[roomtype]*duration
            room_service = self.rooms[room_number]['roomservice']
            print('room bill: Rs.', roombill)
            print('roomservice:Rs.', room_service)
            print('total bill: Rs. ', roombill+room_service)
            del self.rooms[room_number]
        else:
            print(f"room{room_number} is not occupied. ")
    def start_app(self) -> object:
        while True:
            print("___________________")
            print("1) Damal Hotel ")
            print("2) Crawn Hotel")
            print("3) Dholayare Hotel")
            print("4) Exit")
            choosen = input("Enter hotel you need: ")
            if choosen == '1':
                print("you choosen Damal hotel, thank for your booking")
                print("__________________________")
                print("Welcome to Damal hotel")
                print("1) Check-in")
                print("2) Room service")
                print("3) Display Occupied rooms")
                print("4) Check-Out")
                print("5) Exit")
                choice = input("Enter your choice (1-5): ")
                if choice == '1':
                    Name = input("Enter your name: ")
                    Address = input("Enter your adress: ")
                    Phone = input("Enter contec NO: ")
                    self.check_in(Name, Address, Phone)
                elif choice == '2':
                    Room_No = int(input("Enter Room Number: "))
                    self.room_service(Room_No)
                elif choice == '3':
                    self.display_occupied()
                elif choice == '4':
                    room_number = int(input("Enter room number: "))
                    self. check_out(room_number)
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. please try again.")

            elif choosen == '2':
                print("you choosen Crown hotel, thank for your booking")
                print("__________________________")
                print("Welcome to Crown hotel")
                print("1) Check-in")
                print("2) Room service")
                print("3) Display Occupied rooms")
                print("4) Check-Out")
                print("5) Exit")
                choice = input("Enter your choice (1-5): ")
                if choice == '1':
                    Name = input("Enter your name: ")
                    Address = input("Enter your adress: ")
                    Phone = input("Enter contec NO: ")
                    self.check_in(Name, Address, Phone)
                elif choice == '2':
                    Room_No = int(input("Enter Room Number: "))
                    self.room_service(Room_No)
                elif choice == '3':
                    self.display_occupied()
                elif choice == '4':
                    room_number = int(input("Enter room number: "))
                    self. check_out(room_number)
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. please try again.")
            elif choosen == '3':
                print("you choosen Dhoolayare hotel, thank for your booking")
                print("__________________________")
                print("Welcome to Max hotel")
                print("1) Check-in")
                print("2) Room service")
                print("3) Display Occupied rooms")
                print("4) Check-Out")
                print("5) Exit")
                choice = input("Enter your choice (1-5): ")
                if choice == '1':
                    Name = input("Enter your name: ")
                    Address = input("Enter your adress: ")
                    Phone = input("Enter contec NO: ")
                    self.check_in(Name, Address, Phone)
                elif choice == '2':
                    Room_No = int(input("Enter Room Number: "))
                    self.room_service(Room_No)
                elif choice == '3':
                    self.display_occupied()
                elif choice == '4':
                    room_number = int(input("Enter room number: "))
                    self. check_out(room_number)
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. please try again.")
            elif choosen =='4':
                break
            else:
                print("Invalid choosen. please try again")

h = hotel()
h.start_app()


