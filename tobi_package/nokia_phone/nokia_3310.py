def under_construction(name):
    print(f'''
    *****************************************************
                {name}
    *****************************************************
              UNDER
            CONSTRUCTION
    *****************************************************
    ''')


power = int(input('Enter 1 to on the phone: '))
if power == 1:
    print('''
    *****************************************************
                        MENU
    *****************************************************
    1.Phone book
    2.Messages
    3.Chat
    4.Call register
    5.Tones
    6.Settings
    7.Call divert
    8.Games
    9.Calculator
    10.Reminders
    11.Clock
    12.Profiles
    13.Messages
    *****************************************************
        *Select a function using the number beside it*
    *****************************************************
    ''')
    function = int(input('Enter number: '))
    if function == 1:
        print('''
        *****************************************************
                    Phone book
        *****************************************************
        1.Search
        2.Service Nos.
        3.Add name
        4.Erase
        5.Edit
        6.Assign Tone
        7.Send b'card
        8.Options
        9.Speed dials
        10.Voice tags
        *****************************************************
            *Select a function using the number beside it*
        *****************************************************
        ''')
        function = int(input('Enter number: '))
        if function == 1:
            under_construction('Search')
        elif function == 2:
            under_construction('Service Nos.')
        elif function == 3:
            under_construction('Add name')
        elif function == 4:
            under_construction('Erase')
        elif function == 5:
            under_construction('Edit')
        elif function == 6:
            under_construction('Assign tone')
        elif function == 7:
            under_construction("Send b'card")
        elif function == 8:
            print('''
            *****************************************************
                        Options
            *****************************************************
            1.Type of view
            2.Memory status
            *****************************************************
                *Select a function using the number beside it*
            *****************************************************
            ''')
            function = int(input('Enter number: '))
            if function == 1:
                under_construction('Type of view')
            elif function == 2:
                under_construction('Memory status')
            else:
                exit()
        elif function == 9:
            under_construction('Speed dials')
        elif function == 10:
            under_construction('Voice tags')
        else:
            exit()
    elif function == 2:
        print('''
        *****************************************************
                    Messages
        *****************************************************
        1.Write messages
        2.Inbox
        3.Outbox
        4.Picture Messages
        5.Templates
        6.Smileys
        7.Message settings
        8.Info service
        9.Voice mailbox number
        10.Service command editor
        *****************************************************
            *Select a function using the number beside it*
        *****************************************************
        ''')
        function = int(input('Enter number: '))
        if function == 1:
            under_construction('Write messages')
        elif function == 2:
            under_construction('Inbox')
        elif function == 3:
            under_construction('Outbox')
        elif function == 4:
            under_construction('Picture messages')
        elif function == 5:
            under_construction('Templates')
        elif function == 6:
            under_construction('Smileys')
        elif function == 7:
            print('''
            *****************************************************
                        Message settings
            *****************************************************
            1.Set
            2.Common
            *****************************************************
                *Select a function using the number beside it*
            *****************************************************
            ''')
            function = int(input('Enter number: '))
            if function == 1:
                print('''
                *****************************************************
                            Set
                *****************************************************
                1.Message center number
                2.Message sent as
                3.Message validity
                *****************************************************
                    *Select a function using the number beside it*
                *****************************************************
                ''')
                function = int(input('Enter number: '))
                if function == 1:
                    under_construction('Message center number')
                elif function == 2:
                    under_construction('Message sent as')
                elif function == 3:
                    under_construction('Message validity')
                else:
                    exit()
            elif function == 2:
                print('''
                *****************************************************
                            Common
                *****************************************************
                1.Delivery reports
                2.Reply via same center
                3.Character support
                *****************************************************
                    *Select a function using the number beside it*
                *****************************************************
                ''')
                function = int(input('Enter number: '))
                if function == 1:
                    under_construction('Delivery reports')
                elif function == 2:
                    under_construction('Reply via same center')
                elif function == 3:
                    under_construction('Character support')
                else:
                    exit()
            else:
                exit()
        elif function == 8:
            under_construction('Info service')
        elif function == 9:
            under_construction('Voice mailbox number')
        elif function == 10:
            under_construction('Service command editor')
        else:
            exit()
    elif function == 3:
        under_construction('Chat')
    elif function == 4:
        print('''
        *****************************************************
                    Call register
        *****************************************************
        1.Missed calls
        2.Received calls
        3.Dialled numbers
        4.Erase recent call lists
        5.Show call duration
        6.Show call costs
        7.Call cost settings
        8.Prepaid credit
        *****************************************************
           *Select a function using the number beside it*
        *****************************************************
        ''')
        function = int(input('Enter number: '))
        if function == 1:
            under_construction('Missed calls')
        elif function == 2:
            under_construction('Received calls')
        elif function == 3:
            under_construction('Dialled numbers')
        elif function == 4:
            under_construction('Erase recent call lists')
        elif function == 5:
            print('''
            *****************************************************
                        Show call duration
            *****************************************************
            1.Last call duration
            2.All calls duration
            3.Received calls duration
            4.Dialled calls duration
            5.Clear timers
            *****************************************************
               *Select a function using the number beside it*
            *****************************************************
            ''')
            function = int(input('Enter number: '))
            if function == 1:
                under_construction('Last call duration')
            elif function == 2:
                under_construction('All calls duration')
            elif function == 3:
                under_construction('Received calls duration')
            elif function == 4:
                under_construction('Dialled calls duration')
            elif function == 5:
                under_construction('Clear timers')
            else:
                exit()
        elif function == 6:
            print('''
            *****************************************************
                        Show call costs
            *****************************************************
            1.Last call cost
            2.All calls cost
            3.Clear counters
            *****************************************************
               *Select a function using the number beside it*
            *****************************************************
            ''')
            function = int(input('Enter number: '))
            if function == 1:
                under_construction('Last call cost')
            elif function == 2:
                under_construction('All calls cost')
            elif function == 3:
                under_construction('Clear counters')
            else:
                exit()
        elif function == 7:
            print('''
            *****************************************************
                        Call cost settings
            *****************************************************
            1.Call cost limit
            2.Show costs in
            *****************************************************
               *Select a function using the number beside it*
            *****************************************************
            ''')
            function = int(input('Enter number: '))
            if function == 1:
                under_construction('Call cost limit')
            elif function == 2:
                under_construction('Show cost in')
            else:
                exit()
        elif function == 8:
            under_construction('Prepaid credit')
    elif function == 5:
        print('''
        *****************************************************
                    Tones
        *****************************************************
        1.Ringing tone
        2.Ringing volume
        3.Incoming call alert
        4.Composer
        5.Message alert tone
        6.Keypad tones
        7.Warning and game tones
        8.Vibrating alert
        9.Screen saver
        *****************************************************
           *Select a function using the number beside it*
        *****************************************************
        ''')
        function = int(input('Enter number: '))
        if function == 1:
            under_construction('Ringing tone')
        elif function == 2:
            under_construction('Ringing volume')
        elif function == 3:
            under_construction('Incoming call alert')
        elif function == 4:
            under_construction('Composer')
        elif function == 5:
            under_construction('Message alert tone')
        elif function == 6:
            under_construction('Keypad tones')
        elif function == 7:
            under_construction('Warning and game tones')
        elif function == 8:
            under_construction('Vibrating alert')
        elif function == 9:
            under_construction('Screen saver')
    elif function == 6:
        print('''
        *****************************************************
                    Settings
        *****************************************************
        1.Call settings
        2.Phone settings
        3.Security settings
        4.Restore factory settings
        *****************************************************
           *Select a function using the number beside it*
        *****************************************************
        ''')
        function = int(input('Enter number: '))
        if function == 1:
            print('''
            *****************************************************
                        Call settings
            *****************************************************
            1.Automatic redial
            2.Speed dialling
            3.Call waiting options
            4.Own number sending
            5.Phone line in use
            6.Automatic answer
            *****************************************************
               *Select a function using the number beside it*
            *****************************************************
            ''')
            function = int(input('Enter number: '))
            if function == 1:
                under_construction('Automatic Redial')
            elif function == 2:
                under_construction('Speed dialling')
            elif function == 3:
                under_construction('Call waiting options')
            elif function == 4:
                under_construction('Own number sending')
            elif function == 5:
                under_construction('Phone line in use')
            elif function == 6:
                under_construction('Automatic answer')
            else:
                exit()
        elif function == 2:
            print('''
            *****************************************************
                        Phone settings
            *****************************************************
            1.Language
            2.Cell info display
            3.Welcome note
            4.Network selection
            5.Lights
            6.Confirm SIM service actions
            *****************************************************
               *Select a function using the number beside it*
            *****************************************************
            ''')
            function = int(input('Enter number: '))
            if function == 1:
                under_construction('Language')
            elif function == 2:
                under_construction('Cell info display')
            elif function == 3:
                under_construction('Welcome note')
            elif function == 4:
                under_construction('Network selection')
            elif function == 5:
                under_construction('Lights')
            elif function == 6:
                under_construction('Confirm SIM service actions')
            else:
                exit()
        elif function == 3:
            print('''
            *****************************************************
                        Security settings
            *****************************************************
            1.PIN code request
            2.Call barring service
            3.Fixed dialling
            4.Closed user group
            5.Phone security
            6.Change access codes
            *****************************************************
               *Select a function using the number beside it*
            *****************************************************
            ''')
            function = int(input('Enter number: '))
            if function == 1:
                under_construction('PIN code request')
            elif function == 2:
                under_construction('Call  barring service')
            elif function == 3:
                under_construction('Fixed dialling')
            elif function == 4:
                under_construction('Closed user group')
            elif function == 5:
                under_construction('Phone security')
            elif function == 6:
                under_construction('Change access codes')
            else:
                exit()
        elif function == 4:
            under_construction('Restore factory settings')
        else:
            exit()
    elif function == 7:
        under_construction('Call divert')
    elif function == 8:
        under_construction('Games')
    elif function == 9:
        under_construction('Calculator')
    elif function == 10:
        under_construction('Reminders')
    elif function == 11:
        print('''
        *****************************************************
                    Clock
        *****************************************************
        1.Alarm clock
        2.Clock settings
        3.Date settings
        4.Stopwatch
        5.Countdown timer
        6.Auto update of date and time
        *****************************************************
           *Select a function using the number beside it*
        *****************************************************
        ''')
        function = int(input('Enter number: '))
        if function == 1:
            under_construction('Alarm clock')
        elif function == 2:
            under_construction('Clock settings')
        elif function == 3:
            under_construction('Date settings')
        elif function == 4:
            under_construction('Stopwatch')
        elif function == 5:
            under_construction('Countdown timer')
        elif function == 6:
            under_construction('Auto update of date and time')
        else:
            exit()
    elif function == 12:
        under_construction('Profiles')
    elif function == 13:
        under_construction('SIM services')
else:
    exit()
